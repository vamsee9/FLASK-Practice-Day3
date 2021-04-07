from flask import Flask


app = Flask (__name__)


@app.route('/')
def index():
    return "hello world"
@app.route("/saikiran")
def saikiran():
    return"Hello, saikiran!"
@app.route("/python_Flask")
def python_Flask():
    return "2nd elective is, python_Flask"