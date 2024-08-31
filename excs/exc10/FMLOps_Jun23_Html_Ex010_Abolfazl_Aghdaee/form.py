from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class registration(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Enter your username'), Length(min=2, max=20)])
    email = EmailField('Email',validators=[DataRequired('Enter your email'),Email(message='Please enter a valid email address') ])
    password = PasswordField('Password', validators=[DataRequired('Enter your password'), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired('Enter your password again'), Length(min=8, max=20), EqualTo('password', message="your password is not equal to confirm password")])
    submit = SubmitField('Submit')