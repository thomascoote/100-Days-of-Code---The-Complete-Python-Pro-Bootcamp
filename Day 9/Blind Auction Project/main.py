# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from tkinter.font import names

names_dict = {}
names_list = []

def bidding():

    keep_bidding ="y"

    while keep_bidding == "y":
        name = input("Please enter your name\n")
        bid = int(input("Please enter your bid \n$"))

        names_list.append(name)

        # Add Name:Bid to names_dict
        names_dict[name] = bid

        keep_bidding = input("Are there more bids? Y/N\n")
        if keep_bidding == "y":
            print("\n" * 20)



bidding()

print(names_dict["Tom"])

# high_bidder = max(names_dict, key=names_dict.get)
# high_bid = max(names_dict.values())
# print("The highest bid is from", high_bidder, "with a bid of", high_bid)