from flask import render_template, flash, redirect, url_for
from flask_bcrypt import check_password_hash
from stockscreener import app, bcrypt, db
from stockscreener.forms import RegistrationForm, LoginForm
from stockscreener.models import User
from flask_login import login_user, current_user, logout_user

db.create_all()

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/register", methods=['POST', 'GET'])
def register():

    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login", methods=['POST', 'GET'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('root'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('root'))
        else:
            flash(f'Login failed! Please check the email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('root'))
