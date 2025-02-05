import collections.abc

import art
import time
import random

card_dict = {
    "Ace" : 11,
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

your_cards = []
cpu_cards = []
your_aces_held = []
cpu_aces_held = []

def choose_random_card(who):
    chosen_card = random.choice(list(card_dict.keys()))
    print(f"{who} drew {chosen_card}")
    time.sleep(1)
    return chosen_card

def draw_player():
    your_cards.append(choose_random_card("You"))

def draw_cpu():
    cpu_cards.append(choose_random_card("CPU"))

def current_score(n1):
    if n1 == "player":
        your_score = 0
        for i in your_cards:
            your_score += card_dict[i]
        return your_score
    else:
        cpu_score = 0
        for i in cpu_cards:
            cpu_score += card_dict[i]
        return cpu_score

# Draw the initial two cards for the player and the CPU

draw_player()
draw_player()
print(f"Your score: {current_score("player")}")

draw_cpu()
draw_cpu()
print(f"CPU score:{current_score("cpu")}\n")

draw_again = input("Would you like to draw another card? Y/N\n").lower()
while draw_again == "y":
    draw_player()

    print(current_score("player"))
    draw_again = input("Would you like to draw another card? Y/N\n").lower()

print(f"Your cards:{your_cards}")
print(f"Your cards:{cpu_cards}")