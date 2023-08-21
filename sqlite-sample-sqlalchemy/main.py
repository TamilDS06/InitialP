# import sqlite3
# from sqlite3 import OperationalError

# # to create sqlite db in working folder
# db = sqlite3.connect('C:\\My_Folder\\Logics_in_python\\day-63-starting-files-library-project\\sqlite-sample\\books-collection.db')

# # It is like mouse cursor. in order to make changes in db we need to create a cirsor object.
# cursor = db.cursor()

# try:
#     # create table called book.
#     cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, \
#                 author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# except OperationalError as exception:
#     print(exception.args)

# # to add a row(values) into the book table.
# cursor.execute("INSERT INTO books VALUES(1, 'It Started with a Friend Request', 'SUDEEP NAGARKAR', \
#                 '10')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db" # new-books-collection is db's name
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

### CRUD ### C- Create R- Read U- Update D-Delete
# CREATE a record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter.", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
# READ all records
# with app.app_context():
#     results = db.session.execute(db.select(Book).order_by(Book.id))
#     all_books = results.scalars()
#     print(all_books.all())
#     single_book = db.session.execute(db.select(Book).where(Book.title == "It started with friend request")).scalar()
#     # we can get attribute of the class (column(attribute) value of the table(class)) by dot notation
#     print(single_book.id,
#           single_book.title,
#           single_book.author,
#           single_book.rating)
# # UPDATE record by perticular column value
# with app.app_context():
#     update_title = "Harry Potter."
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "The Harry Potter and the Secret of chambers.")).scalar()
#     book_to_update.title = update_title
#     db.session.commit()
# # UPDATE record by perticular id
# with app.app_context():
#     update_title = "The Harry Potter and the Secret of chambers."
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
#     book_to_update.title = update_title
#     db.session.commit()
with app.app_context():
    book_id = 3
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()



