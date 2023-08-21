from turtle import Turtle
from random import randint, choice


class BreakPaddleManager:
    
    def __init__(self, ):
        self.breakpaddles = []


    def create_random_paddle(self):
        if len(self.breakpaddles) == 0:
            y_coordinate = 200
            x_coordinate = -370
            for num in range(0, 13):
                breakpaddle = Turtle()
                breakpaddle.color('white')
                breakpaddle.shape("square")
                breakpaddle.shapesize(stretch_len=2, stretch_wid=1)
                breakpaddle.penup()
                breakpaddle.goto(x_coordinate, y_coordinate)
                self.breakpaddles.append(breakpaddle)
                x_coordinate += 60


    def detect_collision_with_paddle(self, ball):
        for paddle in self.breakpaddles:
            if ball.distance(paddle) <= 24:
                paddle.hideturtle()
            else:
                continue
    