print("Welcome to the Secret Auction!!")

bid_information = {}
index = 1
is_continue = "yes"
maximum_bid = 0
winner_name = ""

while is_continue == "yes" :

    name = input("What is your name? ")
    bid = int(input("What is your bid? ₹"))

    bidder_detail = {
        "name" : name,
        "bid" : bid,
    }

    bid_information[index] = bidder_detail

    is_continue = input("Is their any other bidder. Type 'yes' or 'no'.\n").lower()

    if is_continue == "no" :
        break
    elif is_continue == "yes" :
        index += 1
        print("\n" * 100)
        continue
    else :
        print("You have entered the wrong info. Please enter all details again. ")
        print("\n" * 100)
        continue

for key in bid_information :
    if maximum_bid < bid_information[key]["bid"] :
        maximum_bid = bid_information[key]["bid"]
        winner_name = bid_information[key]["name"]

print("\n" * 50)
print(f"{winner_name} has won this bidding. The bid amount is ₹{maximum_bid}")
