import turtle
from turtle import Turtle, Screen
import random

tutu = Turtle()
turtle.colormode(255)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tutu.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tutu.color(rand_color())
        tutu.circle(100)
        tutu.setheading(tutu.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
