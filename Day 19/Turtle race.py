import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

user_bet= screen.textinput("Place your bet", "Which turtle is going to win ? Choose a color ?")
color =["red", "blue","green", "yellow", "orange","pink"]
y_loc = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtel = Turtle("turtle")
    new_turtel.color(color[turtle_index])
    new_turtel.penup()
    new_turtel.goto(-230,y_loc[turtle_index])
    all_turtles.append(new_turtel)

if user_bet:
    is_race_on = True;

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False;
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color}")
            else:
                print(f"You lose, winner is {winning_color}")
            
        rand_dis = random.randint(0,6)
        turtle.forward(rand_dis)

screen.exitonclick()