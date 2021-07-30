from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

UPLOAD_FOLDER="flasky/static/images/"


app = Flask(__name__)

app.config['SECRET_KEY']='4bfdec5b4ca75b093634d43a07b2520a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///animalTrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['DEBUG']=True


db=SQLAlchemy(app)

login_manager=LoginManager(app)
login_manager.login_view='login'

from livestic import routes

