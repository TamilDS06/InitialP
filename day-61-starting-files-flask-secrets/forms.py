from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class MyLoginForm(FlaskForm):

    email = StringField(label='email', validators=[DataRequired(message="Should not be empty"), Email()])
    password = PasswordField(label='password', validators=[DataRequired(message="Should not be empty"), Length(min=8, max=30, message="Should have atlease 8 charecters.")])
    submit = SubmitField(label="Login")


