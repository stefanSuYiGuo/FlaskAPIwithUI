from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app=app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)

from app.routes import *
