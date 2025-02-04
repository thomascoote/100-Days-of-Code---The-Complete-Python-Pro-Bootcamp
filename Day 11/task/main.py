import collections.abc

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

# print(card_dict[random.choice(list(card_dict.keys()))])

def blackjack():

    your_cards = []

    def choose_random_card():
        chosen_card = random.choice(list(card_dict.keys()))
        print(f"You drew {chosen_card}")
        your_cards.append(chosen_card)
        time.sleep(1)
        score = 0
        for i in your_cards:
            score += (card_dict[i])
            if score > 21:


        print(f"Current score:{score}")

    choose_random_card()
    time.sleep(2)

    choose_random_card()
    time.sleep(2)

    keep_going = input("Would you like to draw again? Y/N").lower()

    while keep_going == "y":

        choose_random_card()
        keep_going = input("Would you like to draw again? Y/N").lower()

    print(your_cards)
blackjack()

