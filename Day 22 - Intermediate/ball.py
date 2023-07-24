from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_step = 10
        self.y_step = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_step *= -1

    def bounce_paddle(self):
        self.x_step *= -1

    def check_bounce_wall(self, screen_height):
        if self.ycor() + 10 >= (screen_height / 2) or self.ycor() - 10 <= (-screen_height / 2):
            self.bounce_wall()

    def check_bounce_paddle(self, paddle):
        if (self.xcor() + 10 == paddle.xcor() or self.xcor() - 10 == paddle.xcor()) and self.distance(paddle) < 50:
            self.bounce_paddle()

    def check_hit_right_wall(self, screen_width):
        return self.xcor() == screen_width / 2 - 10

    def check_hit_left_wall(self, screen_width):
        return self.xcor() == -screen_width / 2 + 10

    def reset_ball(self, side):
        self.goto(0, 0)
        self.x_step = 10 * side
