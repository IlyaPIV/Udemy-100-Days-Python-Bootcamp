from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-25, 25) * 10
        new_car.goto(300, random_y)
        new_car.setheading(180)
        new_car.xcor()
        self.all_cars.append(new_car)

    def move_cars(self, level):
        if random.randint(0, 5) == 1:
            self.create_car()

        for car in self.all_cars:
            car.forward(MOVE_INCREMENT * level + STARTING_MOVE_DISTANCE)
            if car.xcor == -300:
                self.all_cars.remove(car)
                self.create_car()

    def check_for_collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return False
        return True
