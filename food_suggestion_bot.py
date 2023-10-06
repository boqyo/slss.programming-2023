# Food suggestion bot
# Author: shaun
# 6 Oct 2023

# A bot that asks the user what their favorite food is
# will classify that food based off its genre
#will give restaurant suggestion
import random
import time

# Introduce bot
# ask user favorite food
print("Hello, I am here to suggest you a restaurant")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me your favorite food ")
time.sleep(1)

# Italian
italian_food = ["pasta", "pizza"]
NA_food = ["burgers", "hotdogs"]
# If italian,
# suggest italian restaurant
if fave_food.lower().strip("!.,?") in italian_food:
    print("I see you like italian food. I suggest Broli kitchen.")
    time.sleep(1)
    print("Heres their address. 186-8180 No 2 Rd, Richmond, BC V7C 5K1")
elif fave_food.lower().strip("!,.?") in NA_food:
    print("I see you like american classics")
    time.sleep(1)
    print("Try Five Guys. Here is their address.")
    print("635 Robson St, Vancouver, BC V6B 5J3")
else:
    print("Sorry, I'm not sure what kind of food that is")