# Author: Shaun
# date: nov 1 2023
# mcdndalds order and tax

order_cost = 0

burger = int(5)
fries = int(3)

# ask if they want burger fries
# if they want burger fry then add price

burger_ask = input("Do you want burger for 5$ (yes/no) ")
if burger_ask.lower().strip("!,.?") == "yes":
    order_cost += int(5)

fries_ask = input("Do you want fries 3$ (yes/no) ")
if fries_ask.lower().strip("!,.?") == "yes":
    order_cost += int(3)

# add tax
print("your total is", order_cost * 1.14)

