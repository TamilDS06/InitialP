from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    title = StringField("Enter the title of the movie:", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
