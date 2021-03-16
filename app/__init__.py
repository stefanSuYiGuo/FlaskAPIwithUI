from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app=app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config.from_object(Config)

from app.routes import *
