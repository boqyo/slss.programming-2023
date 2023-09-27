# Chatbot
# Author: shaun
# Date: Sep 20 2023
import random
import time
# Greet the user
print("Hello user.")
time.sleep(1)
print("I am a ChatBot, here to talk to you.")
time.sleep(1)
# Get the user's name and store it in a variable
user_name = input("What is your name? ")
time.sleep(0.5)
print(f"Hello, {user_name}")
time.sleep(1)
# Ask the user what their favorite food is
favorite_food = input(f"So, {user_name}, what is your favorite food? ")

# if their favorite food is sushi, reply with yum
if favorite_food == "sushi":
    print("yum 🍣")
    print("I think I love sushi")
elif favorite_food == "burgers" or favorite_food == "Burgers" or favorite_food == "burger" or favorite_food == "Burger":
    time.sleep(0.5)
    print("Burgers are so good")
    time.sleep(1)
    print("Cheeseburgers are my favorite")
else:

# Create a list of possible responses
list_of_food_responses = [
    f"I've had {favorite_food} before. Very good.",
    "That sounds good",
    "Wow, {favorite_food}, good choice."] 

# Choose one of those responses randomly
import random 
random_food_response = random.choice(list_of_food_responses)
# Print out one of those responses
time.sleep(1)
print(random_food_response)