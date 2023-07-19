from turtle import Turtle


class BodyPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = Turtle("square")
        self.body.color("white", "white")
        # self.body.hideturtle()
        self.body.penup()
        self.body.goto(x, y)

    def draw_body(self):
        self.body.forward(10)
        self.body.right(90)
        self.body.forward(10)
        self.body.right(90)
        self.body.forward(20)
        self.body.right(90)
        self.body.forward(20)
        self.body.right(90)
        self.body.forward(20)
        self.body.right(90)
        self.body.forward(10)
        self.body.left(90)
        self.body.back(10)
