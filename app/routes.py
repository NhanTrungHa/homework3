# include Flask class from file flask
from flask import Flask, render_template, flash, redirect, request

# create an instance of Flask class
# __name__ is a predefined setup variable
myobj = Flask(__name__)

name = 'Nhan'
city_names = ['San Jose', 'Los Angeles', 'Tokyo']


# different URL the app will implement
@myobj.route("/")
# called view function
def home():
    return render_template('home.html', city_names=city_names, name=name)


@myobj.route("/", methods=["POST"])
def handle_data():
    form = request.form
    city = request.form.get("cityname")
    flash(city)
    return render_template('home.html', city_names=city_names, name=name, form=form)

myobj.run()
