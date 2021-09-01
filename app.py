from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "home.html"
    )

@app.route("/upload")
def upload_data():
    return render_template(
        "upload.html"
    )

@app.route("/hasil")
def hasil_pencarian():
    return "0"

# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello_there(name = None):
#     return render_template(
#         "home.html",
#         name=name,
#         date=datetime.now()
#     )

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")