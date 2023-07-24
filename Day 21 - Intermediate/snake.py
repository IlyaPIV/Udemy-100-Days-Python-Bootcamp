from body import BodyPart

SEGMENT_SIZE = 20


class Snake:
    def __init__(self):
        self.body = []
        self.direction = "right"
        self.body.append(BodyPart(SEGMENT_SIZE, 0))
        self.body.append(BodyPart(0, 0))
        self.body.append(BodyPart(-SEGMENT_SIZE, 0))
        self.head = self.body[0]
        self.length = 3

    def move_snake(self):
        head = self.body[0]
        tail = self.body.pop(len(self.body) - 1)
        if self.direction == "right":
            tail.body.goto(head.body.xcor() + SEGMENT_SIZE, head.body.ycor())
        elif self.direction == "left":
            tail.body.goto(head.body.xcor() - SEGMENT_SIZE, head.body.ycor())
        elif self.direction == "up":
            tail.body.goto(head.body.xcor(), head.body.ycor() + SEGMENT_SIZE)
        elif self.direction == "down":
            tail.body.goto(head.body.xcor(), head.body.ycor() - SEGMENT_SIZE)
        self.body.insert(0, tail)
        self.head = self.body[0]

    def turn_up(self):
        if self.direction != "down":
            self.direction = "up"

    def turn_down(self):
        if self.direction != "up":
            self.direction = "down"

    def turn_right(self):
        if self.direction != "left":
            self.direction = "right"

    def turn_left(self):
        if self.direction != "right":
            self.direction = "left"

    def increase_snake_size(self):
        tail = self.body[len(self.body) - 1]
        self.body.append(BodyPart(tail.body.xcor(), tail.body.ycor()))
