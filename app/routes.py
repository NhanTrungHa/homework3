# include Flask class from file flask
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    textbox = StringField('City Name', validators=[DataRequired()])
    submit = SubmitField('Submit')


# create an instance of Flask class
# __name__ is a predefined setup variable
myobj = Flask(__name__)

name = 'Nhan'
city_names = ['San Jose', 'Los Angeles', 'Tokyo']


# different URL the app will implement
@myobj.route("/")
# called view function
def home():
    form = LoginForm()
    return render_template('home.html', city_names=city_names, name=name, form=form)


#myobj.run()
