from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

import os



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__)) 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + basedir + "admin.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


# import database model
from admin.models import User


# registration blueprint
from admin.auth.views import auth 
from admin.core.views import core

app.register_blueprint(auth)
app.register_blueprint(core)