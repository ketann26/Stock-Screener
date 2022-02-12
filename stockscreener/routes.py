from flask import render_template, flash, redirect, url_for, request
from flask_bcrypt import check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

from stockscreener import app, bcrypt, db
from stockscreener.forms import RegistrationForm, LoginForm, BuyStockForm
from stockscreener.models import Portfolio, User

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

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('root'))
        else:
            flash(f'Login failed! Please check the email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('root'))

@app.route("/account")
@login_required
def account():
    
    return render_template('account.html', title='Account')

@app.route("/portfolio", methods=['POST', 'GET'])
@login_required
def view_portfolio():

    form = BuyStockForm()
    holdings = Portfolio.query.filter_by(user_id=current_user.id)

    if form.validate_on_submit():

        new_stock = Portfolio(stock=form.stock_name.data, sector=form.sector.data, category=form.category.data,
                                author=current_user)
        db.session.add(new_stock)
        db.session.commit()
        flash('Stock Added to Holdings!', 'success')
        return redirect(url_for('view_portfolio'))
    
    return render_template('portfolio.html', title='Portfolio', form=form, holdings=holdings)

# @app.route("/portfolio/buy", methods=['POST', 'GET'])
# @login_required
# def buy():

#     form = BuyStockForm()

#     if form.validate_on_submit():
#         flash('Stock Added to Holdings!', 'success')
#         return redirect(url_for('view_portfolio'))
#     return render_template('')


# date_added=form.date_added.data, buy=form.buy.data, 