import art
import random
from game_data import data


def random_pick(data_list):
    return random.choice(data_list)


def print_text(pick, its_a):
    name = pick["name"]
    description = pick["description"]
    country = pick["country"]
    if its_a:
        print(f"Compare A: {name}, {description}, from {country}")
    else:
        print(f"Against B: {name}, {description}, from {country}")


def its_true(players_choice, a, b):
    value_a = a["follower_count"]
    value_b = b["follower_count"]
    if players_choice == 'A':
        return value_a > value_b
    else:
        return value_b > value_a


def play_game():
    score = 0
    print(art.logo)
    continue_game = True
    pick_a = random_pick(data)
    data.remove(pick_a)
    while continue_game:
        pick_b = random_pick(data)
        data.remove(pick_b)
        print_text(pick_a, True)
        print(art.vs)
        print_text(pick_b, False)
        choice = input("Who has more followers? Type 'A' or 'B': ")
        if its_true(choice, pick_a, pick_b):
            print("You are right!")
            score += 1
            pick_a = pick_b
            if len(data) == 0:
                print("No more rounds! Sorry! You're WINNER!!!")
                continue_game = False
        else:
            continue_game = False
            print("Sorry, you failed! Game over!")
    print(f"Your score is {score}")


play_game()
