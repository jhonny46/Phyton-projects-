import turtle as t
import random

color = [(252, 222, 190), (250, 162, 66), (244, 197, 127), (234, 67, 76), (76, 53, 76), (11, 46, 77), (146, 61, 78)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100


for _ in range(1, num_of_dots+1):
    tim.dot(20,random.choice(color))
    tim.forward(50)

    if _ % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()