from pickle import GLOBAL, FALSE
from random import randint

import art
import random
import time

# Global Variables

NUMBER_TO_GUESS = randint(1,100)

# Welcome Screen
print(art.logo)

print("Welcome to The Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def difficulty_set():

    difficulty_chosen = False

    while difficulty_chosen == False:

        difficulty = (input("""Select your difficulty, "easy" or "hard"\n""")).lower()

        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Please choose a valid difficulty")

def check_guess(player_guess):
    # Call global variable GUESSES_LEFT
    global GUESSES_LEFT

    if int(player_guess) > NUMBER_TO_GUESS:
        print("Too high")
        GUESSES_LEFT -= 1
        return 0

    if int(player_guess) < NUMBER_TO_GUESS:
        print("Too low")
        GUESSES_LEFT -= 1
        return 0

    if int(player_guess) == NUMBER_TO_GUESS:
        print("Correct!")
        return 1


# Sets the number of lives based on difficulty selection
GUESSES_LEFT = (difficulty_set())
print(f"You have {GUESSES_LEFT} lives remaining")

# TODO Define a function that takes a users input guess and compares it against the stored number.
#   If it's too high, tell the user "Too high" and let them guess again while removing 1 life
#   Same for too low
#   If they guess right, tell them "You guessed correctly!" and end the game


correct_answer = 0

while correct_answer == 0:
    correct_answer = check_guess(input("Please enter your guess\n"))

exit()