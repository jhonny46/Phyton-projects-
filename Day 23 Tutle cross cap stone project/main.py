import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
# create car and move car
    cars.new_car()
    cars.move_cars()

# Detect collusion with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

# FINISH LINE
    if player.is_at_finish_line():
        player.go_to_start()



screen.exitonclick()