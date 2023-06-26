from art import logo


bids_data = {}
print(logo)
print()
another_one = "yes"
while not another_one == "no":
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bids_data[name] = bid
    another_one = input("Anyone else bid? Type 'yes' or 'no':\n")

print(bids_data)
biggest_name = ""
biggest_bid = 0
for key in bids_data:
    curr_bid = bids_data[key]
    if curr_bid > biggest_bid:
        biggest_name = key
        biggest_bid = curr_bid

print(f"Biggest bid is {biggest_bid}, the winner is {biggest_name}")
