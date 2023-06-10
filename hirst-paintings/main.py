# import colorgram
from turtle import Turtle, Screen, colormode
from random import choice

# colors = colorgram.extract('C:\\My_Folder\\Logics_in_python\\hirst-paintings\\image.jpg', 80)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
              (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
              (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170),
              (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78),
              (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169),
              (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]
timmy = Turtle()
colormode(255)
timmy.setheading(220)
timmy.penup()
timmy.forward(300)
timmy.pendown()
timmy.setheading(0)
for i in range(10):
    for j in range(10):
        timmy.dot(20,choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        if j == 9:
            timmy.left(90)
            timmy.penup()
            timmy.forward(50)
            timmy.left(90)
            timmy.forward(500)
            timmy.right(90)
            timmy.right(90)
            timmy.pendown()

screen = Screen()
screen.exitonclick()
