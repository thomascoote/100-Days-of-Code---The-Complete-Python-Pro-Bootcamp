# Prime numbers are divisible by only themselves and 1

def is_prime(num):
    num_list = []
    for i in range(1,num+1):
        if num%i == 0:
            num_list.append(i)
    if len(num_list) == 2:
        print(True)
    else:
        print(False)

is_prime(73)

