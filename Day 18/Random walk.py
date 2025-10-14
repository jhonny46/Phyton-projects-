from turtle import Turtle
import random

draw = Turtle()

jo = Turtle()
color= ["red","orange","yellow","green","blue","indigo","purple"]
heading = [0, 90, 180, 270]
jo.pensize(15)
jo.speed("fastest")
for _ in range(200):
    jo.color(random.choice(color))
    jo.forward(30)
    jo.setheading(random.choice(heading))