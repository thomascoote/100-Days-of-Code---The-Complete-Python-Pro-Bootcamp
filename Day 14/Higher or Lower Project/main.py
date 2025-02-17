from random import random, randint
from tabnanny import check

import game_data
import art

game_data_list = game_data.data
#         'name':
#         'follower_count':
#         'description':
#         'country':


# Welcome Logo
print(art.logo)

score = 0

#Returns a dictionary value from the dictionary list, then removes that entry from the list
def pick_someone():
    game_data_items_count = len(game_data_list) -1
    random_list_index = randint(0, game_data_items_count)
    pick_someone_choice = (game_data_list[random_list_index])
    game_data_list.remove(game_data_list[random_list_index])
    return pick_someone_choice


def highest_followers(first, second):
    if first["follower_count"] > second["follower_count"]:
        return first
    else:
        return second


#Initial picking

choice_a = pick_someone()
choice_b = pick_someone()

#Initial Player Choice

print(f"Compare A: {choice_a["name"]}, a {choice_a["description"]} from {choice_a["country"]}.")
print(art.vs)
print(f"Against B: {choice_b["name"]}, a {choice_b["description"]} from {choice_b["country"]}.")
player_choice = input("Who has more followers, A or B?\n").lower()
if player_choice == "a":
    player_choice = choice_a
    not_chosen = choice_b
else:
    player_choice = choice_b
    not_chosen = choice_a

if player_choice["follower_count"] > not_chosen["follower_count"]:
    print(f"Correct, {player_choice["name"]} from {player_choice["country"]} has {player_choice["follower_count"]} million followers, {not_chosen["name"]} from {not_chosen["country"]} has {not_chosen["follower_count"]} million followers")
    correct_answer = True
else:
    print(f"Wrong, {not_chosen["name"]} from {not_chosen["country"]} has {not_chosen["follower_count"]} million followers, {player_choice["name"]} from {player_choice["country"]} has {player_choice["follower_count"]} million followers")
    correct_answer = False
    print(f"Your final score = {score}")
    exit()

# Carries over the second choice from the previous question to the next question as the first choice
new_first_item = choice_b

#While the player is guessing correctly, this loop will run
while correct_answer == True:
    score += 1
    print(f"Your score is {score}")
    #Randomly picks a new person for the second choice
    new_second_item = pick_someone()

    print(f"Compare A: {new_first_item["name"]}, a {new_first_item["description"]} from {new_first_item["country"]}.")
    print(art.vs)
    print(f"Against B: {new_second_item["name"]}, a {new_second_item["description"]} from {new_second_item["country"]}.")
    player_choice = input("Who has more followers, A or B?\n").lower()

    # If the player choose "a", the dictionary from their selection is added as their choice.
    if player_choice == "a":
        #new_first_item and new_second_item are dictionaries
        player_choice = new_first_item
        not_chosen = new_second_item
    else:
        player_choice = new_second_item
        not_chosen = new_first_item

    if player_choice["follower_count"] > not_chosen["follower_count"]:
        print(f"Correct, {player_choice["name"]} from {player_choice["country"]} has {player_choice["follower_count"]} million followers, {not_chosen["name"]} from {not_chosen["country"]} has {not_chosen["follower_count"]} million followers")
        correct_answer = True
    else:
        print(f"Wrong, {not_chosen["name"]} from {not_chosen["country"]} has {not_chosen["follower_count"]} million followers, {player_choice["name"]} from {player_choice["country"]} has {player_choice["follower_count"]} million followers")
        correct_answer = False
        print(f"Your final score = {score}")
        exit()
    #Moves the second choice to the first choice for the next loop
    new_first_item = new_second_item