from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from break_paddle import BreakPaddleManager
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

r_paddle = Paddle((0, -260))
ball_ = Ball()
score = Scoreboard()
paddlebreak = BreakPaddleManager()


screen.listen()
screen.onkey(fun=r_paddle.right, key='d')
screen.onkey(fun=r_paddle.left, key='a')
paddlebreak.create_random_paddle()

game_is_on = True
while game_is_on:
    start_num_breakpaddles = len(paddlebreak.breakpaddles)
    ball_.move()
    screen.update()
    time.sleep(ball_.move_speed)

    # Detect collision with wall
    if ball_.ycor() > 280:
        # Needs to bounce in y direction
        ball_.bounce_y()
    
    # Detect if the right paddle misses the ball
    if ball_.xcor() > 370 or ball_.xcor() < -370:
        ball_.bounce_x()
        # ball_.reset_position()
        # score.l_point()

    # Detect collision with paddle
    if ball_.distance(r_paddle) < 40:
        # Needs to bounce in x direction
        ball_.bounce_y()
    if len(paddlebreak.breakpaddles) == 0:
        paddlebreak.create_random_paddle()
    paddlebreak.detect_collision_with_paddle(ball_)
    current_num_break_paddles = len(paddlebreak.breakpaddles)
    score_to_add = int(start_num_breakpaddles) - int(current_num_break_paddles)
    score.l_point(score_to_add)


screen.exitonclick()
