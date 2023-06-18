from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    
    def __init__(self):
        self.level = 1
        self.score = Turtle()
        self.score.penup()
        self.score.goto(-250, 250)
        self.score.hideturtle()
        self.score.write(f"Level :{self.level}", align='center', font=FONT)

    def update_score(self):
        self.level += 1
        self.score.clear()
        self.score.write(f"Level :{self.level}", align='center', font=FONT)

    def clear_score(self):
        pass
        # self.score.clear()
