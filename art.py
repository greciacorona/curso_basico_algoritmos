# Recursive art

import turtle

my_turtle = turtle.Turtle()
my_windows = turtle.Screen()

def draw(my_turtle, lenght):
    if lenght > 0:
        my_turtle.forward(lenght)
        my_turtle.right(90)
        draw(my_turtle, lenght-10)

draw(my_turtle, 100)
my_windows.exitonclick()