import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player_ = Player()
carmanager = CarManager()
score = Scoreboard()

screen.onkey(fun=player_.move_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_random_car()
    carmanager.move_cars()
    if carmanager.detect_collision_with_car(player_):
        game_is_on = False
    if player_.finish():
        carmanager.levelup()
        score.update_score()

screen.exitonclick()
