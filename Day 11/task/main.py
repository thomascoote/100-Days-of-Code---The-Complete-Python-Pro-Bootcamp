import art
import time
import random

card_dict = {
    "Ace" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "Jack": 10,
    "Queen": 10,
    "King" : 10,
}

print(art.logo)
print("Welcome to Blackjack!")


def blackjack():


    def choose_random_card():
        chosen_card = random.choice(list(card_dict.keys()))
        n1 = (card_dict[chosen_card])
        return n1

    card_1 = int(choose_random_card())
    print(f"You drew a {card_1}")
    time.sleep(2)

    card_2 = int(choose_random_card())
    print(f"You drew a {card_2}")
    time.sleep(2)

    score = card_1 + card_2
    print(score)

    keep_going = input("Would you like to draw again? Y/N").lower()

    while keep_going == "y":

blackjack()

