from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddBook(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired(message="Should not be empty")])
    author_name = StringField("Author Name", validators=[DataRequired(message="Should not be empty")])
    rating = StringField("Rating", validators=[DataRequired(message="Should not be empty")])
    submit = SubmitField(type='submit')

class ChangeRating(FlaskForm):
    rating = IntegerField("New rating", validators=[DataRequired(message="Should not be empty")])
    submit = SubmitField(type='submit')