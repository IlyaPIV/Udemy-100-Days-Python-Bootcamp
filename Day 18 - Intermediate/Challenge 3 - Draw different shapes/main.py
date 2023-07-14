import turtle as t


tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

for sides in range(3, 11):
    angle = 360 / sides
    for i in range(sides):
        t.forward(100)
        t.right(angle)


screen = t.Screen()
screen.exitonclick()
