from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        # self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(350, -250)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        # self.goto(100, 200)
        # self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self, score_to_add):
        self.l_score += score_to_add
        self.update_score()

    # def r_point(self):
    #     self.r_score += 1
    #     self.update_score()
