# encoding: utf-8
"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://adminbot:poker444@db4free.net/pspt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 60
db = SQLAlchemy(app)
import mercadorias3.models
import mercadorias3.views
