from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", bg=fg)
    tick_label.config(text="", bg=fg)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    short_sec_break = SHORT_BREAK_MIN * 60
    long_sec_break = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    if reps % 2 == 0 and reps < 8:
        timer_label.config(text="Break", bg=PINK)
        count_down(short_sec_break)  # http://tcl.tk/man/tcl8.6/TclCmd/after.htm
    elif reps % 8 == 0 and reps < 8:
        timer_label.config(text="Break", bg=RED)
        count_down(long_sec_break)
    else:
        timer_label.config(text="Work", bg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'  # https://stackoverflow.com/questions/11328920/is-python-strongly-typed
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # http://tcl.tk/man/tcl8.6/TclCmd/after.htm
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += '✓'
            tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)  # https://colorhunt.co/  (famous color's website)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

fg = GREEN
timer_label = Label(text='Timer', bg=fg, font=(FONT_NAME, 33))
timer_label.grid(row=0, column=1)
tick_label = Label(bg=fg, font=(FONT_NAME, 33))
tick_label.grid(row=2, column=1)
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
