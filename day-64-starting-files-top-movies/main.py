from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from forms import RateMovieForm, AddMovie


MOVIE_DB_API_KEY = "NOT_A_REAL_KEY"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movie-collection.db"
Bootstrap5(app)
# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)


# create model for table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False) # Should be Integer field.
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False) # Should be Float field.
    ranking = db.Column(db.Integer, nullable=False) # Should be Integer field.
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'
    

#create table
with app.app_context():
    db.create_all()

# with app.app_context():
    # first_movie = Movie(
    #             title="Phone Booth",
    #             year=2002,
    #             description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #             rating=7.3,
    #             ranking=10,
    #             review="My favourite character was the caller.",
    #             img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    #             )
    # second_movie = Movie(
    #             title="Avatar The Way of Water",
    #             year=2022,
    #             description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #             rating=7.3,
    #             ranking=9,
    #             review="I liked the water.",
    #             img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    #         )
    # db.session.add(first_movie)
    # db.session.add(second_movie)
    # db.session.commit()


@app.route("/")
def home():
    # SQLalchemy "Query the Data Doc!"
    # https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#query-the-data
    results = db.session.execute(db.select(Movie).order_by(Movie.id))
    all_movies = results.scalars()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies.all())


@app.route("/edit", methods=['POST', 'GET'])
def rate_movie():
    movie_id = request.args.get('id')
    movie_to_change = db.session.execute(db.select(Movie).where(Movie.id == int(movie_id))).scalar()
    form = RateMovieForm()
    if request.method == 'POST':
        # movie_to_change = db.session.execute(db.select(Movie).where(Movie.id == int(movie_id))).scalar()
        movie_to_change.rating = request.form['rating']
        movie_to_change.review = request.form['review']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_to_change, form=form)
    

@app.route("/delete")
def remove():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == int(movie_id))).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data

        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

        
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        
        # Redirect to /edit route
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
