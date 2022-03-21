# include Flask class from file flask
from flask import Flask, render_template, flash, redirect, request
from forms import LoginForm


# create an instance of Flask class
# __name__ is a predefined setup variable
myobj = Flask(__name__)

myobj.config['SECRET KEY'] = 'secrfgdgret'

name = 'Nhan'
city_names = ['San Jose', 'Los Angeles', 'Tokyo']


# different URL the app will implement
@myobj.route("/")
# called view function
def home():
    return render_template('home.html', city_names=city_names, name=name)


@myobj.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

myobj.run()
