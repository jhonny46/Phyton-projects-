import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    random_colors = (r,g,b)
    return random_colors
tim.speed("fastest")

def draw_circle(gap_size):
    for draw in range( int (360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap_size)

draw_circle(40)
screen = t.Screen()
screen.exitonclick()