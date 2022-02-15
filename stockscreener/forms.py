from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import DecimalField
from wtforms.validators import Length, ValidationError, Length, DataRequired, Email, EqualTo
from stockscreener.models import User

class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username has been taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email has been taken. Please choose another one.')

class LoginForm(FlaskForm):

    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class BuyStockForm(FlaskForm):

    stock_name = StringField('Stock Name', validators=[DataRequired()])
    sector = SelectField('Sector', choices=[('default', '-Select Sector-'),
                                            ('auto', 'Automobile'),
                                            ('chem', 'Chemicals'),
                                            ('comm', 'Communication'),
                                            ('const', 'Construction'),
                                            ('consum', 'Consumer Durables'),
                                            ('diversified', 'Diversified'),
                                            ('energy', 'Energy'),
                                            ('eng', 'Engineering'),
                                            ('fin', 'Financial'),
                                            ('fmcg', 'FMCG'),
                                            ('pharma', 'Healthcare'),
                                            ('insur', 'Insurance'),
                                            ('metal', 'Metals'),
                                            ('service', 'Services'),
                                            ('tech', 'Technology'),
                                            ('textile', 'Textiles'),
                                            ('others', 'Others')])
    category = SelectField('Category', choices=[('default', '-Select Category-'),
                                                ('large', 'Large Cap'),
                                                ('mid', 'Mid Cap'),
                                                ('small', 'Small Cap')])
    date_added = DateField('Date Added')
    buy = DecimalField('Buy Price')
    buy_btn = SubmitField('Buy')

class SellStockForm(FlaskForm):

    sell_id = HiddenField('Hidden Table Row ID')
    sell_btn = SubmitField('Sell')


