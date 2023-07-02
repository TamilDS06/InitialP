from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.label_score = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, padx=20, pady=20, font=('Arial', 10))
        self.label_score.grid(row=0, column=1)
        self.canvas_1 = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas_1.create_text(
            150,
            125,
            width=200,
            text="Dummy",
            fill=THEME_COLOR,
            font=('Arial', 10, 'italic'))
        self.canvas_1.grid(column=0, row=1, pady=50, padx=20, columnspan=2)
        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_1.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas_1.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas_1.itemconfig(self.question_text, text="You have reached maximum questions.")
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer('False'))

    def get_feedback(self, result):
        if result:
            self.canvas_1.config(bg='green')
        else:
            self.canvas_1.config(bg='red')
        self.label_score.config(text=f"Score:{self.quiz.score}")
        self.window.after(1000, func=self.get_next_question)
