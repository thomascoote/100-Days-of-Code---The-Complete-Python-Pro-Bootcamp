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

highest_bid = 0
highest_bidder = ""

for i in names_dict:
    bid_amount = names_dict[i]

    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = i

print(highest_bidder)
print(highest_bid)




# print(names_dict["Tom"])

#For each Kay:Value pair in the "names_dict" dictionary, find the highest Value
#and store the associated Key as "high_bidder"
#
# high_bidder = max(names_dict, key=names_dict.get)
# high_bid = max(names_dict.values())
# print("The highest bid is from", high_bidder, "with a bid of", high_bid)