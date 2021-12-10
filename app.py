from flask import Flask, render_template
from login import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9ad31e48816f68f953e9214654a140a7'

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/register")
def register():

    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
    

if __name__ == '__main__':
    app.run(debug=True)