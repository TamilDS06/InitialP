from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

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

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)
# create model for table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
#create table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    results = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = results.scalars()
    return render_template('index.html', all_books=all_books.all())


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        # new_book = {
        #     'title': request.form['title'],
        #     'author': request.form['author'],
        #     'rating': request.form['rating']
        # }
        # with app.app_context():
        new_book = Book(title=request.form['title'], 
                        author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/change_rating", methods=['GET', 'POST'])
def change_rating():
    if request.method == 'POST':
        # return render_template('add.html')
        book_id = request.form['id']
        book_to_change_rating = db.session.execute(db.select(Book).where(Book.id == int(book_id))).scalar()
        book_to_change_rating.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_to_change_rating = db.session.execute(db.select(Book).where(Book.id == int(book_id))).scalar()
    return render_template('change_rating.html', book=book_to_change_rating)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == int(book_id))).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")

