from turtle import Turtle

FONT = ("Arial", 40, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def update_score(self, left, right):
        self.l_score += left
        self.r_score += right
        self.clear()
        self.write_score()

    def check_winner(self):
        return self.r_score < 5 and self.l_score < 5

    def print_winner(self):
        self.goto(0, 0)
        self.clear()
        if self.r_score > self.l_score:
            winner = "RIGHT PLAYER WINS"
        else:
            winner = "LEFT PLAYER WINS"
        self.write(winner, align=ALIGNMENT, font=FONT)
