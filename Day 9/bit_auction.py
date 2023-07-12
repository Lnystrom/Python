import bitmap

print(bitmap.logo)

biding = {}


def high_value(biding_record):
    """Function that returns the name and the highest value"""
    highest_bid = 0
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

Rolando = True

while Rolando:
    name = input("Insert you name: ")
    bid = int(input("Insert your biding price: $ "))
    biding[name] = bid
    repeat = input("Other users want to bid? ")
    if repeat == "y":
        print(bitmap.clear)


    else:
        Rolando = False
        print(bitmap.clear)
        high_value(biding)
