from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.y_random = None
        self.x_random = None
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.x_random = random.randint(-280, 280)
        self.y_random = random.randint(-280, 280)
        self.goto(self.x_random, self.y_random)
