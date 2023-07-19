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
        self.tail = self.body[2]
        self.length = 3

    def move_snake(self):
        head = self.body[0]
        tail = self.body.pop(self.length - 1)
        if self.direction == "right":
            tail.body.goto(head.body.xcor() + SEGMENT_SIZE, head.body.ycor())
        elif self.direction == "left":
            tail.body.goto(head.body.xcor() - SEGMENT_SIZE, head.body.ycor())
        elif self.direction == "up":
            tail.body.goto(head.body.xcor(), head.body.ycor() + SEGMENT_SIZE)
        elif self.direction == "down":
            tail.body.goto(head.body.xcor(), head.body.ycor() - SEGMENT_SIZE)
        self.body.insert(0, tail)

    def turn_up(self):
        self.direction = "up"

    def turn_down(self):
        self.direction = "down"

    def turn_right(self):
        self.direction = "right"

    def turn_left(self):
        self.direction = "left"
