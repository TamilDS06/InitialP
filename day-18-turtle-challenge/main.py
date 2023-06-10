from turtle import Turtle, Screen, colormode
from random import randint, choice

timmy_turtle = Turtle()


# To change the shape and change(set) a color
# timmy_turtle.shape("turtle")
# timmy_turtle.color("red")

# To draw a square
# for i in range(0,4):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)

# To draw dashed line
# for i in range(0, 50):
#     timmy_turtle.pendown()
#     timmy_turtle.forward(20)
#     timmy_turtle.penup()
#     timmy_turtle.forward(20)

# To draw 2D shapes from a size 3 to 9
# list_shapes = [3, 4, 5, 6, 7, 8, 9, 10]
# colormode(255)
# for i in range(0, len(list_shapes)):
#     shape = list_shapes[i]
#     angle = 360 / shape
#     timmy_turtle.color(randint(0, 255),
#                        randint(0, 255),
#                        randint(0, 255))
#     for j in range(0, shape):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(angle)

# To make turtle to g random walk
# timmy_turtle.width(10)
# timmy_turtle.speed("fastest")
# turn = [0, 90, 180, 270]
# colormode(255)
# for i in range(200):
#     timmy_turtle.color(randint(0, 255),
#                        randint(0, 255),
#                        randint(0, 255))
#     timmy_turtle.right(turn[randint(0, 3)])
#     timmy_turtle.forward(25)
#     timmy_turtle.right(turn[randint(0, 3)])
#     timmy_turtle.forward(25)

# To draw a funky circle
def gen_color_():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


colormode(255)
is_on = True
angle = 30
radius = 100
timmy_turtle.speed("fastest")
for i in range(0, int(360/angle)):
    timmy_turtle.color(gen_color_())
    timmy_turtle.left(angle)
    timmy_turtle.circle(radius)

screen = Screen()
screen.exitonclick()