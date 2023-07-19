from turtle import Screen, Turtle
from snake import Snake
import time


def prepare_screen(snk):
    scr = Screen()
    scr.setup(width=600, height=600)
    scr.bgcolor("black")
    scr.title("My Snake Game")
    scr.tracer(0)
    scr.listen()
    scr.onkey(key="Up", fun=snk.turn_up)
    scr.onkey(key="Down", fun=snk.turn_down)
    scr.onkey(key="Left", fun=snk.turn_left)
    scr.onkey(key="Right", fun=snk.turn_right)
    return scr









snake = Snake()

screen = prepare_screen(snake)

game_is_on = True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
