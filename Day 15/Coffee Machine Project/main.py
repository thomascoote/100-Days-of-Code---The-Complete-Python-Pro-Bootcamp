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
    print(f"Water = {resources["water"]}\n")
    print(f"Milk = {resources["milk"]}\n")
    print(f"Coffee = {resources["coffee"]}\n")
    print(f"Money = ${resources["money"]:.2f}\n")

def user_selection():
    valid_selection = False
    while valid_selection == False:
        user_selection = input("What would you like? (espresso/latte/cappuccino):").lower()
        for i in MENU:
            if user_selection == i or user_selection == "off":
                valid_selection = True
        if valid_selection == False and user_selection != "report":
            print("Try again")
        if user_selection == "off":
            exit()
        if user_selection == "report":
            report()
    return user_selection

def check_against_resources(drink_selected, current_resources):
    current = current_resources
    required = MENU[drink_selected]["ingredients"]
    #Check if any resource is 0 or below
    for i in required:
        if current[i] - required[i] <= 0:
            print(f"Sorry there is not enough {i}")
            exit()
    #Update the values of current resources
    for i in required:
        current[i] -= required[i]

def coin_input(drink_selected, current_resources):
    change_due = 0.00
    current = current_resources
    cost = MENU[drink_selected]["cost"]
    quarters = float(input("How many quarters?")) * 25
    dimes = float(input("How many dimes?")) * 10
    nickels = float(input("How many nickels?")) * 5
    pennies = float(input("How many pennies"))

    money_paid = (quarters+dimes+nickels+pennies)/100

    if money_paid >= cost:
        change_due = float(money_paid - cost)
        current["money"] += (money_paid - change_due)

        return change_due
    else:
        print("Sorry that's not enough money. Money refunded.")
        exit()

keep_running = True

while keep_running == True:

    drink_choice = user_selection()
    check_against_resources(drink_choice, resources)

    change = coin_input(drink_choice, resources)
    print(f" Here is ${change:.2f} in change. Here is your {drink_choice} \U0001f600. Enjoy!")




