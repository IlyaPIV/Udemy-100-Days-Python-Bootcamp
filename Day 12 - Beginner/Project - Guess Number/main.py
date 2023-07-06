import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def init_attempts(diff):
    if diff == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_guessed(number, target, attempts_left):
    if number == target:
        print("You got it! Correct answer!")
        return 0
    elif number < target:
        print("Too low")
    elif number > target:
        print("Too high")
    return attempts_left - 1


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    target_number = random.randint(1, 100)
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = init_attempts(difficult)
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number")
        guessed = int(input("Make a guess: "))
        attempts = check_guessed(guessed, target_number, attempts)
        if attempts == 0:
            if guessed != target_number:
                print(f"You've run out of guesses, you lose. The number was {target_number}")
        else:
            print("Guess again")


game()
