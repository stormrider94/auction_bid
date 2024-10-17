import os
from art import logo
all_bidders = []

def start_the_bid():
    print(f"\n {logo}")
    print("\n Welcome to the secret auction program")
    new_bidder = True

    while new_bidder:
        name = input("\n What is your name?: ")
        bid = input("\n What's your bid? : $ ")
        continue_bidding = input("\n Are there any other bidders? Type 'yes' or 'no' : ")
        current_bidder = {}
        current_bidder["name"] = name
        current_bidder["bid"] = bid
        all_bidders.append(current_bidder)

        if continue_bidding == 'no':
            new_bidder = False

    #clear the console
    os.system('cls')

    all_bidders_sorted = sorted(all_bidders,key=lambda x : float(x["bid"]), reverse= True)
    winner = all_bidders_sorted[0]
    print(all_bidders_sorted)
    print(f"\nThe highest bidder(the ultimate winner) is {winner['name']} with a bid of ${winner['bid']}")

start_the_bid()