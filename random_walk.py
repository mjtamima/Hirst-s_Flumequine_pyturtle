import random
import turtle
from turtle import Turtle, Screen

tutu = Turtle()
turtle.colormode(255)


def rand_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)


tutu.pensize(10)
tutu.speed("fast")
angles = [0, 90, 180, 270]
for _ in range(500):
    tutu.color(rand_color())
    tutu.forward(20)
    tutu.setheading(random.choice(angles))

