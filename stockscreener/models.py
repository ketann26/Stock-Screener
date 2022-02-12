from sqlalchemy.orm import backref, lazyload
from stockscreener import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    holdings = db.relationship('Portfolio', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(50), unique=False, nullable=False)
    sector = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    # date_added = db.Column(db.DateTime(), nullable=False)
    # buy = db.Column(db.Float(), nullable=False)
    # cmp = db.Column(db.Float(), nullable=True)
    # p_l = db.Column(db.Float(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Portfolio('{self.stock}', '{self.sector}', '{self.category}')"

