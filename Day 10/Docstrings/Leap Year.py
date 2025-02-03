from xmlrpc.client import Boolean

"""
- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder   
"""


year = 1904

leap_year = False

def is_leap_year(year):

    if year%4 == 0:
        # print(f"{year}/4 = {year/4}. First test passed")
        leap_year = True
        # print(f"Current leap_year value = {leap_year}")

        if year%100 == 0:
            # print(f"Mod 100 test passed")
            leap_year = False
            # print(f"Current leap_year value = {leap_year}")

            if year%400 == 0:
                # print(f"Mod 400 test passed")
                leap_year = True
                # print(f"Current leap_year value = {leap_year}")
    else:
        # print(f"{year}/4 = {year / 4}. First test failed")
        leap_year = False
        # print(f"Current leap_year value = {leap_year}")


    print(leap_year)


is_leap_year(year)