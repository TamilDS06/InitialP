from flask import Flask
from random import randint


def gen_random_number():
    return randint(0, 9)


random_number = gen_random_number()

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Guess a number between 0 to 9</h1> \
            <img src='https://media.giphy.com/media/mFD8YeF2sEQBIvrBF4/giphy.gif' \
            alt='All the best' width='500', height='300'>"

@app.route('/<int:number>')
def check_with_eandom_number(number):
    if number == random_number:
        return "<h1 style 'color:Green;'>You found me!</h1> \
                <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' \
                alt='All the best', width='500', height='300'>"
    elif number > random_number:
        return "<h1 style 'color:Red;'>Too high!Try again</h1> \
                <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' \
                width='500', height='300'>"
    elif number < random_number:
        return "<h1 style 'color:Yellow;'>Too Low!Try again</h1> \
                <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' \
                width='500', height='300'>"
    else:
        return "<h1>None</h1>"
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="5000")