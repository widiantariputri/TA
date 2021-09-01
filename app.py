from logging import debug
from flask import Flask
from datetime import datetime
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
                return redirect(url_for('hasil_pencarian'))
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




@app.route("/hasil", methods=['GET', 'POST'])
def hasil_pencarian():
    return ('<h1> Ini hasil hahahaha </h1>')


if __name__ == '__main__':
    app.run(debug=True)
