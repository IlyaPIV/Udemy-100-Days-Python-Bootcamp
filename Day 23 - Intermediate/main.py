import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()

screen = Screen()
screen.title("Tutle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
car_manager.create_car()

scoreboard = Scoreboard()

level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars(level)
    screen.update()
    game_is_on = car_manager.check_for_collision(player)
    if player.is_crossed():
        level += 1
        scoreboard.write_score(level)
        player.reset_to_start()
scoreboard.game_over()
screen.exitonclick()
