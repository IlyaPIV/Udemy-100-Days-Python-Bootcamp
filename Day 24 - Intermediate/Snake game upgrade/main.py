from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
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
food = Food()
scoreboard = ScoreBoard()
screen = prepare_screen(snake)

game_is_on = True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.25)
    if snake.head.distance(food) < 15:
        food.goto_random_point()
        snake.increase_snake_size()
        scoreboard.increase_score()
    if snake.head.body.xcor() >= 300 or snake.head.body.xcor() <= -300 or snake.head.body.ycor() >= 300 or snake.head.body.ycor() <= -300:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    for segment in snake.body[1:]:
        if snake.head.body.distance(segment.body) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
