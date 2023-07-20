from turtle import Turtle


class BodyPart:
    def __init__(self, x, y):
        self.body = Turtle("square")
        self.body.color("white", "white")
        # self.body.hideturtle()
        self.body.penup()
        self.body.goto(x, y)

    def distance(self, food):
        return self.body.distance(food)
