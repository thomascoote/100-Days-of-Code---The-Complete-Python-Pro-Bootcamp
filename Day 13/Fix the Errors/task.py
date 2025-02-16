driving_age = 18

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Value error")
    age = int(input("How old are you?"))


if age < 18:
    print(f"You can drive at age {driving_age}.")
else:
    print("You are old enough to drive")
