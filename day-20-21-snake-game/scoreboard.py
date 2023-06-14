from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 8, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.Score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.Score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.Score += 1
        self.clear()
        self.update_scoreboard()
