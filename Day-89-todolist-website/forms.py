from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class AddTaskForm(FlaskForm):

    name = StringField(label='Name of your task', validators=[DataRequired(message="Should not be empty")])
    start_date = StringField(label='Starting date of the task', validators=[DataRequired(message="Should not be empty")])
    end_date = StringField(label='Ending date of the task', validators=[DataRequired(message="Should not be empty")])
    status = IntegerField(label='Status of the task', validators=[DataRequired(message="Should not be empty")])
    submit = SubmitField(label="Add")