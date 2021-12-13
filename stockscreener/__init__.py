from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ad31e48816f68f953e9214654a140a7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userbase.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from stockscreener import routes