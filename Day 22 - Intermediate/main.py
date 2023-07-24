import time

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def game_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong")
    screen.tracer(0)
    screen.listen()
    return screen


game_screen = game_screen()
paddle_right = Paddle(360, 0)
paddle_left = Paddle(-360, 0)
game_screen.onkey(paddle_right.go_up, "Up")
game_screen.onkey(paddle_right.go_down, "Down")
game_screen.onkey(paddle_left.go_up, "w")
game_screen.onkey(paddle_left.go_down, "s")
ball = Ball()
score_board = ScoreBoard()

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.05)
    ball.move_ball()
    ball.check_bounce_wall(SCREEN_HEIGHT)
    ball.check_bounce_paddle(paddle_right)
    ball.check_bounce_paddle(paddle_left)
    if ball.check_hit_left_wall(SCREEN_WIDTH):
        ball.reset_ball(1)
        score_board.update_score(0, 1)
    if ball.check_hit_right_wall(SCREEN_WIDTH):
        ball.reset_ball(-1)
        score_board.update_score(1, 0)
    game_is_on = score_board.check_winner()
score_board.print_winner()

game_screen.exitonclick()
