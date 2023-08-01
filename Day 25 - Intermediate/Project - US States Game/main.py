import turtle

import pandas

from states_helper import StatesHelper
from turtle import Screen


def get_mouse_coors_on_click(x, y):
    print(x, y)


helper = StatesHelper()
map_image = "blank_states_img.gif"

screen = Screen()
screen.title("U.S. States Game")
screen.screensize(725, 491)
screen.addshape(map_image)

turtle.shape(map_image)
turtle.onscreenclick(get_mouse_coors_on_click)

score = helper.get_score()
while score < 50:
    curr_title = str(score) + "/50: Guess the State"
    input_state = screen.textinput(title=curr_title, prompt="What's another state's name?")
    if input_state == "Exit":
        missing_states = helper.missed_states()
        print(f"Missing states are: {missing_states}")
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    helper.check_state(input_state)
    score = helper.get_score()

turtle.mainloop()
