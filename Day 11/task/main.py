import collections.abc

import art
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

your_cards = []
cpu_cards = []
your_score = 0
cpu_score = 0
your_aces = 0
cpu_aces = 0
# Draw the initial two cards for the player and the CPU

def draw(who):
    choice = random.choice(list(card_dict.keys()))
    print(f"{who} drew a {choice}")
    return choice

def update_scores(cards1, cards2):
    score1 = 0
    score2 = 0
    for i in cards1:
        score1 += card_dict[i]
    for i in cards2:
        score2 += card_dict[i]
    return score1, score2


your_cards.append(draw("You"))
print(your_cards)

your_cards.append(draw("You"))
print(your_cards)

cpu_cards.append(draw("cpu"))
print(cpu_cards)

cpu_cards.append(draw("cpu"))
print(cpu_cards)

print(f"Your score = {update_scores(your_cards,cpu_cards)[0]}\n CPU score = {update_scores(your_cards,cpu_cards)[1]}")

player_draw_again = "y"
cpu_draw_again = "y"

player_draw_again = input("Would you like to draw another card? y/n\n").lower()

while player_draw_again == "y":
    your_aces = 0
    your_cards.append(draw("You"))
    print(your_cards)
    update_scores(your_cards, cpu_cards)
    your_score = update_scores(your_cards,cpu_cards)[0]
    for i in your_cards:
        if i == "Ace":
            your_aces += 1

    if your_score > 21:
        if your_aces == 1:
            your_score -= 10
            if your_score > 21:
                if your_aces == 2:
                    your_score -= 10

    if your_score > 21:
        print(f"Your score = {your_score} \nBUST")
        exit()

    print(f"Your score = {your_score}\n")

    cpu_score = update_scores(your_cards, cpu_cards)[1]
    for i in cpu_cards:
        if i == "Ace":
            cpu_aces += 1

    if cpu_score > 21:
        if cpu_aces == 1:
            cpu_score -= 10
            if cpu_score > 21:
                if cpu_aces == 2:
                    cpu_score -= 10

    if cpu_score < 17:
        cpu_cards.append(draw("cpu"))
        cpu_score = update_scores(your_cards, cpu_cards)[1]
    print(cpu_cards)
    print(f"CPU score = {cpu_score}")

    player_draw_again = input("Would you like to draw another card? y/n\n").lower()

