import art

print(art.logo)

def add(n1, n2):
    return (n1) + (n2)

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

counter = 0
keep_going = "n"
while counter == 0:

    if keep_going == "n":
        n1 = int(input("First number:"))
    elif keep_going == "y":
        n1 = answer
    else:
        exit()
    n2 = int(input("Second number:"))

    print("Choose an operation:")
    for i in operations:
        print(i)

    operation = input("Choose an operation")

    answer = operations[operation](n1,n2)
    print(answer)
    keep_going = input(f"Press Y to continue calculating with {answer} or N to start over:\n").lower()
