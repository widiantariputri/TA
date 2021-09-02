from logging import debug
from flask import Flask
from datetime import datetime
from ANP import ANP
from SAW import SAW
import re
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './UPLOADS'
ALLOWED_EXTENSIONS = ['csv']



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.debug = True
app.secret_key = 'ayut'


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/bobot")
def bot_kepentingan():
    return render_template("bobot.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        # check jika file berhasil diraih
        if request.files:
            fi = request.files['file']
            if fi.filename == '':
                flash('tidak ada file')
                return redirect(request.url)
            if allowed_file(fi.filename):
                print('allowed')
                filename = secure_filename(fi.filename)
                fi.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('hasil_pencarian', filename=filename))
                print('sukses')
            else:
                flash('Extension is not supported' )
                return redirect(request.url)
    print('gagal')
    return render_template(
        "upload.html"
    )

def allowed_file(filename):
    if not '.' in filename:
        return False
    ext = filename.split('.', 1)[1]
    print(ext)
    if ext in app.config['ALLOWED_EXTENSIONS']:
        return True
    else:
        return False




@app.route("/hasil/<filename>", methods=['GET', 'POST'])
def hasil_pencarian(filename):
    DDIR = 'UPLOADS/'+filename
    SURVEY_DATA = 'DATASET/ANOTHER_RESPONDEN.csv'

    anp = ANP(DDIR,SURVEY_DATA)

    gem = anp.get_gm()
    cluster_gm = anp.get_cluster_gm()

    matrix = anp.get_matrix()

    eigen_vector, anp_sum_col = anp.get_eigen(matrix)

    lambda_max = anp.get_lambda(eigen_vector, anp_sum_col)

    anp_ci, anp_cr = anp.get_ci_cr( lambda_max, matrix)

    eigen_alter = anp.get_eigen_alter()



    # the 'cluster' part-------

    cluster_mat = anp.get_cluster_matrix()

    cluster_eigen_vector, cluster_sum_col = anp.get_eigen(cluster_mat)

    cluster_lambda_max = anp.get_lambda(cluster_eigen_vector, cluster_sum_col)

    cluster_ci, cluster_cr = anp.get_ci_cr( cluster_lambda_max, cluster_mat)

    # unweighted matrix
    unweighted_mat = anp.get_unweighted_mat(matrix,eigen_alter)


    saw = SAW()
    hasil_saw = saw.get_hasil()
    return render_template('result.html', hasil=hasil_saw)


if __name__ == '__main__':
    app.run(debug=True)
