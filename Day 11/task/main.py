import collections.abc
import time

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
your_aces = 0
cpu_aces = 0
# Draw the initial two cards for the player and the CPU

def initial_draw():
    your_score = 0
    cpu_score = 0
    #Your Cards
    your_cards.append(random.choice(list(card_dict.keys())))
    your_cards.append(random.choice(list(card_dict.keys())))
    for i in your_cards:
        your_score += card_dict[i]
    print("Your Hand")
    print(your_cards)
    print("Your Score")
    print(your_score)

    cpu_cards.append(random.choice(list(card_dict.keys())))
    print("CPU Hand")
    print(cpu_cards, "*")
    cpu_cards.append(random.choice(list(card_dict.keys())))
    for i in cpu_cards:
        cpu_score += card_dict[i]

    if len(your_cards) == 2 and your_score == 21:
        print("Player Blackjack!")
        exit()
    if len(cpu_cards) == 2 and cpu_score == 21:
        print("CPU Blackjack!")
        exit()


initial_draw()

draw_again = input("Would you like to draw another card? y/n?").lower()
while draw_again == "y":
    your_score = 0
    your_cards.append(random.choice(list(card_dict.keys())))
    for i in your_cards:
        your_score += card_dict[i]


    for i in your_cards:
        if i == "Ace":
            your_aces +=1

    if your_score > 21 and your_aces == 1:
        your_score -= 10
    if your_score > 31 and your_aces == 2:
        your_score -= 20

    print("Your Hand")
    print(your_cards)
    time.sleep(1)
    print("Your Score")
    print(your_score)
    time.sleep(1)

    if your_score > 21:
        print("Bust!")
        exit()

    draw_again = input("Would you like to draw again? y/n").lower()

cpu_score = 0
for i in cpu_cards:
    cpu_score += card_dict[i]

while cpu_score < 17:
    new_cpu_card = []
    new_cpu_card.append(random.choice(list(card_dict.keys())))
    for i in new_cpu_card:
        cpu_score += card_dict[i]

    for i in cpu_cards:
        if i == "Ace":
            your_aces +=1

    if cpu_score > 21 and cpu_aces == 1:
        cpu_score -= 10
    if cpu_score > 31 and cpu_aces == 2:
        cpu_score -= 20

    cpu_cards.append(new_cpu_card[0])
    print(f"CPU Hand = {cpu_cards}")
    time.sleep(1)
    print(f"CPU Score = {cpu_score}")

    if cpu_score > 21:
        print("CPU Bust!")
        time.sleep(1)
        exit()

# Calculate the final scores and decide who won

your_final_score = 0
cpu_final_score = 0
for i in your_cards:
    your_final_score += card_dict[i]
for i in cpu_cards:
    cpu_final_score += card_dict[i]

if cpu_final_score < your_final_score < 22:
    print(your_cards)
    time.sleep(1)
    print("Player Wins!")
elif your_final_score < cpu_final_score < 22:
    print(cpu_cards)
    time.sleep(1)
    print("CPU Wins!")
else:
    print("Draw!")

time.sleep(1)

exit()
