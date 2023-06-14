from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
snake_ = Snake()
food_ = Food()
score = ScoreBoard()
screen.listen()
screen.onkey(fun=snake_.up, key="Up")
screen.onkey(fun=snake_.down, key="Down")
screen.onkey(fun=snake_.right, key="Right")
screen.onkey(fun=snake_.left, key="Left")

screen.tracer(0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_.move()

    # detect collision with food
    if snake_.head.distance(food_) < 15:
        food_.refresh()
        snake_.extend()
        score.increase_score()

    # detect collision with wall
    if snake_.head.xcor() > 280 or snake_.head.xcor() < -280 or snake_.head.ycor() > 280 or snake_.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with own tail
    for segment in snake_.segments[1:]:
        if snake_.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()
screen.exitonclick()
