import turtle as t
import random

jo = t.Turtle()
color= ["red","orange","yellow","green","blue","indigo","purple"]

def draw_sides(sides):
    angle = 360 / sides
    jo.speed(20)
    for _ in range(sides):
        jo.pendown()
        jo.width(5)
        jo.forward(100)
        jo.right(angle)

for _ in range(3,27):
    jo.color(random.choice(color))
    draw_sides(_)