# from tkinter import *
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(height=600, width=500)
#
# my_label = Label(text="My first label", font=('Arial', 24, "bold"))
# my_label.pack(side='right')  # https://docs.python.org/3/library/tkinter.html#the-packer,
#
#
# # https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
#
#
# def change_label():
#     new_text = input_.get()
#     # my_label['text'] = "Changed label"
#     my_label.config(text=new_text)
#
#
# button_ = Button(text="Click here", command=change_label)
# button_.pack()
# # http://tcl.tk/man/tcl8.6/TkCmd/entry.htm
# input_ = Entry(width=15)
# input_.pack()
#
#
# window.mainloop()


from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)
#
# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
#
# # Buttons
# def action():
#     print("Do something")
#
#
# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Gets current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()


# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)

# buttons
button = Button(text="Click Me1")
button.config(padx=20, pady=20)
button.grid(row=1, column=1)


button = Button(text="Click Me2")
button.grid(row=0, column=2)


# Get input
input_ = Entry(width=10)
print(input_.get())
input_.grid(row=3, column=3)

window.mainloop()