import colorgram
import random
import turtle as t


def extract_colors():
    extracted_colors = colorgram.extract("dots.jpg", 35)

    list_of_colors = []
    for col in extracted_colors:
        rgb = col.rgb
        list_of_colors.append((rgb.r, rgb.g, rgb.b))

    print(list_of_colors)
    return list_of_colors


def get_color():
    return random.choice(colors_list)


def move_to_start(br):
    br.penup()
    br.back(150)
    br.right(90)
    br.forward(150)
    br.left(90)


def shift_to_next_line(br):
    br.penup()
    br.back(400)
    br.left(90)
    br.forward(40)
    br.right(90)
    br.pendown()


colors_list = extract_colors()

screen = t.Screen()
screen.colormode(255)
brush = t.Turtle()
brush.speed(10)
brush.hideturtle()
move_to_start(brush)
for x in range(10):
    for y in range(10):
        brush.dot(20, get_color())
        brush.penup()
        brush.forward(40)
        brush.pendown()
    shift_to_next_line(brush)


screen.exitonclick()
