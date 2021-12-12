from flask import render_template, flash, redirect, url_for
from stockscreener import app
from stockscreener.forms import RegistrationForm, LoginForm


@app.route("/")
def root():
    return render_template('index.html')

@app.route("/register", methods=['POST', 'GET'])
def register():

    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'Account created successfully for { form.username.data }', 'success')
        return redirect(url_for('root'))
    
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login", methods=['POST', 'GET'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@test.com' and form.password.data == 'password':
            flash(f'You have been logged in', 'success')
            return redirect(url_for('root'))
        else:
            flash(f'Login failed! Please check the email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)
