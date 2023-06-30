############### Blackjack Project #####################


from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(cards_set):
    if len(cards_set) == 2:
        if cards_set[0] + cards_set[1] == 21:
            return 0
    score = sum(cards_set)
    if 11 in cards_set and score > 21:
        cards_set.remove(11)
        cards_set.append(1)
        score -= 10
    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21 and computer_score > 21:
        return "Draw - you both wen over"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    is_game_over = False
    user_cards = []
    computer_cards = []
    users_score = -1
    comp_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(logo)
    while not is_game_over:
        users_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print(f"> Player's start cards: {user_cards} - current score is {users_score}")
        print(f"> Dealer's first card is : {computer_cards[0]}")

        if users_score == 0 or comp_score == 0 or users_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score is {users_score}")
    print(f"Comp final hand: {computer_cards}, final score is {comp_score}")
    print(compare(users_score, comp_score))


play_game()
while input("Do you want to play another one game of Blackjack? Type 'yes' to continue: ") == "yes":
    play_game()
