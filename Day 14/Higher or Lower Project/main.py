from tabnanny import check

import game_data
import art

#         'name':
#         'follower_count':
#         'description':
#         'country':


# Welcome Logo
print(art.logo)

# The input for this function is the index of the FIRST dictionary you want to grab the data from
def compare_a(dict_number):
    temp_dict_a = game_data.data[dict_number]
    print(f"Compare A: {temp_dict_a["name"]}, a {temp_dict_a["description"]}, from {temp_dict_a["country"]}")

# The input for this function is the index of the SECOND dictionary you want to grab the data from
def compare_b(dict_number):
    temp_dict_b = game_data.data[dict_number]
    print(f"Against B: {temp_dict_b["name"]}, a {temp_dict_b["description"]}, from {temp_dict_b["country"]}")

def check_answer(value_1, value_2, users_answer):
    a_dict = game_data.data[value_1]
    b_dict = game_data.data[value_2]
    a = game_data.data[value_1]["follower_count"]
    b = game_data.data[value_2]["follower_count"]
    if a > b:
        highest_followers = "a"
        highest_dict = a_dict
        lowest_dict = b_dict
    else:
        highest_followers = "b"
        highest_dict = b_dict
        lowest_dict = a_dict

    if users_answer == highest_followers:
        print(f"Correct! {highest_dict["name"]} has {highest_dict["follower_count"]} million followers, {lowest_dict["name"]} only has {lowest_dict["follower_count"]} million followers\n")
        return True
    else:
        print(f"Wrong! {highest_dict["name"]} has {highest_dict["follower_count"]} million followers, {lowest_dict["name"]} only has {lowest_dict["follower_count"]} million followers\n")
        return False

correct_guess = True
dict_increment = 0
score = 0

while correct_guess == True:

    # Track and print current score
    print(f"Your current score is {score}")

    compare_a(dict_increment)
    print(art.vs)
    compare_b(dict_increment+1)

    user_choice = input("Who has more followers? Type A or B:\n").lower()

    correct_guess = check_answer(dict_increment, dict_increment+1, user_choice)
    if correct_guess == True:
        score += 1
    #Increment the dictionaries to cycle through by 1
    dict_increment += 1

