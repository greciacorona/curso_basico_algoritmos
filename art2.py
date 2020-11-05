# Recursive art

import turtle

my_turtle = turtle.Turtle()
my_windows = turtle.Screen()

def draw(my_turtle, lenght):
    if lenght:
        my_turtle.forward(lenght)
        my_turtle.left(123)
        draw(my_turtle, lenght-2)

if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    screen = turtle.Screen()

    colors = (
        '#006699',
        '#006666',
        '#660066',
        '#990000',
        '#ad3270',
        '#e65100',
        '#1a237e',
        '#827717',
        '#006064',
        '#f57f17',
        '#d50000',
        '#4a148c',
    )

    for color in colors:
        my_turtle.pencolor(color)
        draw(my_turtle, 100)

    my_windows.exitonclick()