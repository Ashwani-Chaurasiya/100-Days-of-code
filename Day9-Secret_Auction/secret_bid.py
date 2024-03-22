from art import logo
print(logo)
import os

bids = {}
bidder = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidder:
    bidder_name = input("Enter the Bidder's Name: ")
    bid_amount = int(input("Enter the bid amount: "))
    bids[bidder_name] = bid_amount
    any_bidder = input("Is there is another bidder? If Yes type 'Yes' else type 'No'.\n").lower()
    if any_bidder == "no":
        bidder = False
        find_highest_bidder(bids)
    elif any_bidder == 'yes':
        os.system('cls')
        
    
    
            