from turtle import Turtle, Screen
import random

tutu = Turtle()
screen = Screen()

def random_color():
    screen.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    tutu.color(R, G, B)

def draw_shapes(turns):
    tutu.pensize(2)
    angle = 360 / turns
    for _ in range(turns):
        tutu.forward(80)
        tutu.right(angle)

for i in range(3, 11):
    random_color()
    draw_shapes(i)


screen.exitonclick()
