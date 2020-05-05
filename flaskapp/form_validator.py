from flask_wtf import FlaskForm

from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('re_password')])
    re_password = PasswordField('re_password', validators=[DataRequired()])


class RegistrationForm(Form):
    userid = StringField('User ID', [validators.Length(min=4, max=25)])
    username = StringField('User Name', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    re_password = PasswordField('Repeat Password', validators=[DataRequired()])
    # accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
