from flask import Flask
from config import Config

myobj = Flask(__name__)

myobj.config.from_mapping(
    SECRET_KEY='you - will - never - guess'
)

from app import routes
