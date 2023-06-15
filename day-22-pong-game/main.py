from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball_ = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.up, key='Up')
screen.onkey(fun=r_paddle.down, key='Down')
screen.onkey(fun=l_paddle.up, key='w')
screen.onkey(fun=l_paddle.down, key='s')

game_is_on = True
while game_is_on:
    ball_.move()
    screen.update()
    time.sleep(ball_.move_speed)

    # Detect collision with wall
    if ball_.ycor() > 280 or ball_.ycor() < -280:
        # Needs to bounce in y direction
        ball_.bounce_y()

    # Detect collision with paddle
    if ball_.distance(r_paddle) < 50 and ball_.xcor() > 350 or ball_.distance(l_paddle) < 50 and ball_.xcor() < -350:
        # Needs to bounce in x direction
        ball_.bounce_x()
    
    # Detect if the right paddle misses the ball
    if ball_.xcor() > 370:
        ball_.reset_position()
        score.l_point()

    # Detect if the right paddle misses the ball
    if ball_.xcor() < -370:
        ball_.reset_position()
        score.r_point()
        
screen.exitonclick()
