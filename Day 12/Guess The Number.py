from pickle import GLOBAL
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


# Sets the number of lives based on difficulty selection
GUESSES_LEFT = (difficulty_set())
print(f"You have {GUESSES_LEFT} lives remaining")

# TODO Choose a number between 1 and 100 and store it in a variable
# Define a function that takes a users input guess and compares it against the stored number.
#   If it's too high, tell the user "Too high" and let them guess again while removing 1 life
#   Same for too low
#   If they guess right, tell them "You guessed correctly!" and end the game

check_guess(input("Please enter your guess"))