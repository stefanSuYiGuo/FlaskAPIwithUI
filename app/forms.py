from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    # The way to name the function must be validate_xxx. And xxx here must be a variable in RegisterForm class
    def validate_username(self, username):
        print(username.data)
        print(User.query.filter_by(username=username.data).first())
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken, please choose another one.')

    def validate_email(self, email):
        # print(email.data)
        # print(User.query.filter_by(username=email.data).first())
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('Email already taken, please choose another one.')
