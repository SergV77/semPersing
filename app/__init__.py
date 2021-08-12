import os.path
from flask import Flask
from flask_bootstrap import Bootstrap




basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object("config")
bootstrap = Bootstrap(app)

from app import views


