from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

screen.tracer(0)

ball = Ball()
l_paddel = Paddle((350,0))
r_paddel = Paddle((-350,0))

screen.listen()
screen.onkey(l_paddel.go_up ,"Up")
screen.onkey(l_paddel.go_down,"D"
                              "own")
screen.onkey(r_paddel.go_up,"w")
screen.onkey(r_paddel.go_down,"s")


is_game_on = True

while is_game_on:
    screen.update()

screen.exitonclick()



