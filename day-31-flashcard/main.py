from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# create random word from data.csv
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(Title_text_f, text="French", fill='black')
    canvas.itemconfig(Word_text_f, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_image, image=back_card_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(Title_text_f, text="English", fill='white')
    canvas.itemconfig(Word_text_f, text=current_card['English'], fill='white')


def is_known():
    to_learn.remove(current_card)
    data_ = pandas.DataFrame(to_learn)
    data_.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# Screen
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Card
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card_image = PhotoImage(file='./images/card_front.png')
back_card_image = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 258, image=front_card_image)
Title_text_f = canvas.create_text(400, 150, text='French', fill='black', font=("Ariel", 40, 'italic'))
Word_text_f = canvas.create_text(400, 263, text='Word', fill='black', font=("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2, pady=25, padx=25)

# Buttons
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, padx=50, pady=50, command=is_known)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, padx=50, pady=50, command=next_card)
wrong_button.grid(row=1, column=1)
next_card()

window.mainloop()
