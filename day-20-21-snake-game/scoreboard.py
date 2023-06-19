from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 8, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.Score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.Score} High Score :{self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.Score > self.high_score:
            self.high_score = self.Score
        self.Score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.Score += 1
        self.update_scoreboard()
