from turtle import Turtle, Screen


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_clockwise():
    # timmy.right(30)
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_counter_clockwise():
    # timmy.left(30)
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


timmy = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
