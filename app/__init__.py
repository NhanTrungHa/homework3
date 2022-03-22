from flask import Flask

myobj = Flask(__name__)

myobj.config.from_mapping(
    SECRET_KEY='you - will - never - guess'
)

myobj.config['SECRET_KEY'] = 'you - will - never - guess'
myobj.secret_key
from app import routes
