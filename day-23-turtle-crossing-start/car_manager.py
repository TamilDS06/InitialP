from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    
    def __init__(self, ):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_random_car(self):
        create_random_choice = randint(1,6)
        if create_random_choice == 6:
            car = Turtle()
            car.color(choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            y_coordinate = randint(-250, 250)
            x_coordinate = 300
            car.goto(x_coordinate, y_coordinate)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def levelup(self):
        self.car_speed += MOVE_INCREMENT

    def detect_collision_with_car(self, player):
        game_over = False
        for car in self.cars:
            if player.distance(car) <= 24:
                say_game_over = Turtle()
                say_game_over.write("Game Over", align='center', font=("Arial", 15, "normal"))
                game_over = True
            else:
                continue
        return game_over
