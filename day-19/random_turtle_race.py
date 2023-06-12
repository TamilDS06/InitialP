from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=600, height=800)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["yellow", "blue", "green", "red", "purple", "orange"]
is_race_on = False
if user_input:
    is_race_on = True
# timmy = Turtle(shape="turtle")
index = 0
y = -300
turtle_list = []
for i in range(0, 6):
    timmy = Turtle(shape="turtle")
    turtle_list.append(timmy)
    timmy.color(color_list[i])
    timmy.penup()
    timmy.goto(x=-250, y=y)
    y += 100
    index += 1
while is_race_on:
    for turtle_ in turtle_list:
        if turtle_.xcor() > 770:
            is_race_on = False
            if turtle_.pencolor() == user_input:
                print(f"You've won. The winning color is {turtle_.pencolor()}")
            else:
                print(f"You've lost. The winning color is {turtle_.pencolor()}")
        random_distance = randint(0, 10)
        turtle_.forward(random_distance)

screen.exitonclick()
