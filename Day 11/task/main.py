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
your_aces_held = 0
cpu_aces_held = 0

def choose_random_card(who):
    player_aces = 0
    cpu_aces = 0
    chosen_card = random.choice(list(card_dict.keys()))
    print(f"{who} drew {chosen_card}")
    if chosen_card == "Ace" and who == "player":
        player_aces += 1
    if chosen_card == "Ace" and who == "CPU":
        cpu_aces += 1
    time.sleep(1)
    return chosen_card, player_aces, cpu_aces

def draw_player():
    your_cards.append(choose_random_card("player")[0])
    player_aces = choose_random_card("player")[1]

def draw_cpu():
    cpu_cards.append(choose_random_card("CPU")[0])
    cpu_aces = choose_random_card("CPU")[1]
def current_score(n1):
    if n1 == "player":
        your_score = 0
        for i in your_cards:
            your_score += card_dict[i]
        if your_aces_held > 0 and your_score > 21:
            your_score -= 10
        return your_score
    else:
        cpu_score = 0
        for i in cpu_cards:
            cpu_score += card_dict[i]
        if cpu_aces_held > 0 and cpu_score > 21:
            cpu_score -= 10

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
    if current_score("player") > 21:
        print("Bust!")
        exit()

    draw_again = input("Would you like to draw another card? Y/N\n").lower()

print(f"Your cards:{your_cards}")
print(f"CPU cards:{cpu_cards}")