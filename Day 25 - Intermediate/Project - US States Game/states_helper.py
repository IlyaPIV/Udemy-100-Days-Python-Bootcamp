import pandas
from turtle import Turtle


class StatesHelper(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.already_guessed = []
        self.all_states = self.data.state.to_list()
        print(self.all_states)
        self.hideturtle()
        self.penup()

    def is_new_value(self, state_name):
        corrected_name = state_name
        if corrected_name in self.already_guessed:
            print("You have already guessed this value")
        elif corrected_name not in self.all_states:
            print("Incorrect input value")
        else:
            self.already_guessed.append(state_name)
            self.check_state(state_name)

    def check_state(self, state_name):
        states_data = self.data[self.data.state == state_name]
        print(states_data)
        self.goto(int(states_data.x), int(states_data.y))
        self.write(states_data.state.item())

    def get_score(self):
        return len(self.already_guessed)

    def missed_states(self):
        missing_states = []
        for state in self.all_states:
            if state not in self.already_guessed:
                missing_states.append(state)
        return missing_states
