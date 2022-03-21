from flask import Flask

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess'
)

from app import routes