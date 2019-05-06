from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length, Email
from .models import User
from datetime import date

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = Killers.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = Killers.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')