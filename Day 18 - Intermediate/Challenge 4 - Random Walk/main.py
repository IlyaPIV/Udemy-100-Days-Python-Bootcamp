import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

screen = t.Screen()
screen.delay(5)


def pick_color():
    return random.choice(colours)


for i in range(50):
    tim.pen(pencolor=pick_color(), pensize=10)
    tim.setheading(random.randint(0, 4) * 90)
    tim.forward(20)

screen.exitonclick()
