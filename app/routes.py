# include Flask class from file flask
from flask import Flask, render_template, flash, redirect, request

# create an instance of Flask class
# __name__ is a predefined setup variable
myobj = Flask(__name__)

name = 'Nhan'
city_names = ['San Jose', 'Los Angeles', 'Tokyo']

myobj.config.from_mapping(
    SECRET_KEY='you - will - never - guess'
)

myobj.config['SECRET_KEY'] = 'you - will - never - guess'


# different URL the app will implement
@myobj.route("/", methods=['GET', 'POST', 'PUT'])
# called view function
def home():
    form = request.form
    if request.form.get("cityname") is not None:
        city = request.form.get("cityname")
        flash(city)
    return render_template('home.html', city_names=city_names, name=name)


myobj.run()
