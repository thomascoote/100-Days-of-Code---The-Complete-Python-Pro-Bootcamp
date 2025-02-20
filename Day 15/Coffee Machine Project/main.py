from tabnanny import check

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": float(0.00),
}

available_commands = ["cappucino", "latte", ]

def report():
    print(f"Water = {resources["water"]}\n"
          f"Milk = {resources["milk"]}\n"
          f"Coffee = {resources["coffee"]}\n"
          f"Money = ${resources["money"]:.2f}\n")

def user_selection():
    valid_selection = False
    while valid_selection == False:
        user_selection = input("What would you like? (espresso/latte/cappuccino):").lower()
        for i in MENU:
            if user_selection == i or user_selection == "off":
                valid_selection = True
        if valid_selection == False:
            print("Try again")
        if user_selection == "off":
            exit()
    return user_selection

def check_against_resources(drink_selected, current_resources):
    water_check = current_resources["water"] - MENU[drink_selected]["ingredients"]["water"]
    milk_check = current_resources["milk"] - MENU[drink_selected]["ingredients"]["milk"]
    coffee_check = current_resources["coffee"] - MENU[drink_selected]["ingredients"]["coffee"]

    #Add each check into a list so we can loop through and check if >0

    check_resource_list = [water_check,milk_check,coffee_check]
    for i in check_resource_list:
        if i <= 0:
            print("Not enough resources")
            return False
        else:
            return True

def coin_input():
    quarters = input("How many quarters?").lower()
    dimes = input("How many dimes?").lower()
    nickels = input("How many nickels?").lower()
    pennies = input("How many pennies").lower()
#TODO 2 - Check selection against current machine resources - Done
# Not enough = "Sorry not enough {resource} and exit
# Enough = "Please insert coins"

# User inputs their drink choice. Choice is stored as variable "drink_choice""
drink_choice = user_selection()

# Resources needed to make drink checked against current resource levels.
check_against_resources(drink_choice, resources)



# How to find the resource value for the desired drink
# print(MENU[drink_choice]["ingredients"]["water"])

#TODO 3 - Allow input of how many quarters, dimes, nickles and pennies are inserted
# Store the current coins deposited in the transaction and check against price of selected drink.
# If enough, print success message, update resources and return to choice
# If not enough, print refund message and return to choice



