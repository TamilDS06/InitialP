from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
               'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char1 in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char2 in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)  # https://pypi.org/project/pyperclip/


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password_ = input_password.get()
    if len(password_) == 0 or len(password_) == 0:
        messagebox.showwarning(title="Warning", message="Don't let any field empty:")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details:\nWebsite :{website}\nEmail :"
                                                              f"{email}\nPassword :{password_}")
        if is_ok:
            with open('data.txt', mode='a') as file_write:
                file_write.write(f'{website} | {email} | {password_}\n')
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=450, height=300)  # https://tkdocs.com/tutorial/canvas.html

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=tomato_image)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:", font=('Arial', 10))
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=('Arial', 10))
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=('Arial', 10))
password_label.grid(row=3, column=0)

# Entries
input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()  # https://tkdocs.com/tutorial/widgets.html#entry
input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "mts@gmailcom")
input_password = Entry(width=22)
input_password.grid(row=3, column=1)

# Buttons
button_generate_password = Button(text="Generate password", command=gen_pass)
button_generate_password.grid(row=3, column=2)
button_add = Button(text="Add", width=30, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
