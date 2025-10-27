from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")

screen.tracer(0)
scoarboard = Scoreboard()

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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with padel
    if ball.distance(l_paddel) < 50 and ball.xcor() > 320 or ball.distance(r_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddel
    if ball.xcor() > 380:
        ball.reset_position()
        scoarboard.l_point()
    # Detect l paddel
    if ball.xcor() < -380:
        ball.reset_position()
        scoarboard.r_point()

screen.exitonclick()



