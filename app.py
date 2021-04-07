import datetime
from flask import Flask, render_template


app = Flask (__name__)


@app.route('/')
def index():  
     now = datetime.datetime.now()
     new_year = now.month==1 and now.day ==1
     return render_template("index.html",new_year=new_year)
#     headline = "hello, saikiran!!"             #
#     return render_template("index.html", headline=headline)

# @app.route("/bye")
# def bye():
#     headline = "Good bye!"
#     return render_template("index.html", headline=headline)
     

   
   
    #return "hello world"
# # @app.route("/saikiran")
# # def saikiran():
# #     return"Hello, saikiran!"
# # @app.route("/python_Flask")
# # def python_Flask():
# #     return "2nd elective is, python_Flask"
# @app.route("/<string:name>")# will print message for string what we are giving 
# def hello(name):
#     name = name.capitalize()
#     return f"<h1>Hello, {name}!</h1>"