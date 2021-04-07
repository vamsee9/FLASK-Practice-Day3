from flask import Flask


app = Flask (__name__)


@app.route('/')
def index():
    return "hello world"
# @app.route("/saikiran")
# def saikiran():
#     return"Hello, saikiran!"
# @app.route("/python_Flask")
# def python_Flask():
#     return "2nd elective is, python_Flask"
@app.route("/<string:name>")# will print message for string what we are giving 
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"