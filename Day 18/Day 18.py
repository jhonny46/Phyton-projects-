from turtle import Turtle

draw = Turtle()


for _ in range(15):
    draw.pendown()
    draw.forward(10)
    draw.penup()
    draw.forward(10)
