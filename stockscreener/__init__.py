from flask import Flask
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '9ad31e48816f68f953e9214654a140a7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userbase.db'

db = SQLAlchemy(app)

from stockscreener import routes