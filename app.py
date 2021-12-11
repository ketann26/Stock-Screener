from flask import Flask, render_template, flash, url_for, redirect
from flask.helpers import url_for
from login import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9ad31e48816f68f953e9214654a140a7'

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

if __name__ == '__main__':
    app.run(debug=True)