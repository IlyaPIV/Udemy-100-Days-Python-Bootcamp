from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def init_turtles_to_start():
    our_turtles = []
    for x in range(6):
        col = random.choice(colors)
        colors.remove(col)
        t = Turtle(shape="turtle")
        t.color(col)
        t.penup()
        t.goto(x=-380, y=(-200 + x*80))
        our_turtles.append(t)
    return our_turtles


def race_turtles():
    while True:
        for t in turtles:
            step = random.randint(0, 10)
            t.forward(step)
            if t.xcor() == screen.window_width() / 2 - 20:
                return t.pencolor()


screen = Screen()
screen.setup(width=800, height=600)
users_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = init_turtles_to_start()
winner = race_turtles()
if winner == users_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")
screen.exitonclick()
