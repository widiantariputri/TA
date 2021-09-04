from logging import debug
from flask import Flask
from datetime import datetime
from ANP import ANP
from SAW import SAW
import re
from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import os
import pandas as pd
import numpy as np

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


@app.route("/bobot", methods=['GET', 'POST'])
def bot_kepentingan():

    dataset_name = session.get('dataset')
    dataset = pd.read_csv('UPLOADS/'+str(dataset_name))
    subkriteria = np.array(dataset.columns[2:])

    # kriteria yg tersedia
    kriteria = ['Measurable', 'Capital', 'Alternative']

    if request.method == 'POST':
        print('POST!')

        # Getting the kriteria and sub kriteria
        # range input
        kriteria_input_value = request.form.getlist('kriteria-list[]')
        subkriteria_input_value = request.form.getlist('sub-list[]')

        # Getting the dropdown bobot input
        bobot_from = request.form.getlist('bobot_kriteria_from[]')
        bobot_to = request.form.getlist('bobot_kriteria_to[]')

        # Getting the dropdown sub input
        sub_from = request.form.getlist('sub_from[]')
        sub_to = request.form.getlist('sub_to[]')

        # Turning it into dictionary (object) so it can be easily
        # stored and accessed via session
        bobot_form = dict()
        bobot_form['from'] = bobot_from
        bobot_form['to'] = bobot_to

        sub_form = dict()
        sub_form['from'] = sub_from
        sub_form['to'] = sub_to

        session['bobot_form'] = bobot_form
        session['sub_form'] = sub_form
        session['kriteria_range'] = kriteria_input_value
        session['subkriteria_range'] = subkriteria_input_value

        return redirect(url_for('hasil_pencarian'))
    else:
        # subkriteria didapat dari dataset

        return render_template("bobot.html",
                               context={'kriteria': kriteria,
                                        'subkriteria': subkriteria})


@ app.route("/upload", methods=['GET', 'POST'])
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
                context = {
                    'filename': filename}
                fi.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                session['dataset'] = filename
                return redirect(url_for('bot_kepentingan'))
            else:
                flash('Extension is not supported')
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


@ app.route("/hasil/", methods=['GET', 'POST'])
def hasil_pencarian():
    '''
    DDIR = 'UPLOADS/'+filename
    SURVEY_DATA = 'DATASET/ANOTHER_RESPONDEN.csv'

    anp = ANP(DDIR, SURVEY_DATA)

    gem = anp.get_gm()
    cluster_gm = anp.get_cluster_gm()

    matrix = anp.get_matrix()

    eigen_vector, anp_sum_col = anp.get_eigen(matrix)

    lambda_max = anp.get_lambda(eigen_vector, anp_sum_col)

    anp_ci, anp_cr = anp.get_ci_cr(lambda_max, matrix)

    eigen_alter = anp.get_eigen_alter()

    # the 'cluster' part-------

    cluster_mat = anp.get_cluster_matrix()

    cluster_eigen_vector, cluster_sum_col = anp.get_eigen(cluster_mat)

    cluster_lambda_max = anp.get_lambda(cluster_eigen_vector, cluster_sum_col)

    cluster_ci, cluster_cr = anp.get_ci_cr(cluster_lambda_max, cluster_mat)

    # unweighted matrix
    unweighted_mat = anp.get_unweighted_mat(matrix, eigen_alter)

    saw = SAW()
    hasil_saw = saw.get_hasil()
    return render_template('result.html', hasil=hasil_saw)
    '''

    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
