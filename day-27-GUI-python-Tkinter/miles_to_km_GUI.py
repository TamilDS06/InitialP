from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to kiloMeter converter")
window.minsize(width=50, height=50)
window.config(padx=20, pady=20)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)


miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)


km_label = Label(text="Km")
km_label.grid(row=1, column=2)

input_1 = Entry(width=24)
input_1.grid(row=0, column=1)
label_4 = Label()
label_4.grid(row=1, column=1)


def convert_miles_to_km():
    user_input_miles = int(input_1.get())
    print(type(user_input_miles))
    km = int(user_input_miles) * 1.60934
    label_4.config(text=km)


# calls action() when pressed
button_calculate = Button(text="Calculate", command=convert_miles_to_km)
button_calculate.grid(row=2, column=1)


window.mainloop()
