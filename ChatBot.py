# Chatbot
# Author: shaun
# Date: Sep 20 2023

# Greet the user
print("Hello user.")
print("I am a ChatBot, here to talk to you.")
# Get the user's name and store it in a variable
user_name = input("What is your name? ")
print(f"Hello, {user_name}")
# Ask the user what their favorite food is
favorite_food = input(f"So, {user_name}, what is your favorite food? ")
# Make a comment about their food
# Create a list of possible responses
list_of_food_responses = [
    f"I've had {favorite_food} before. Very good.",
    "That sounds good",
    "I'll never be able to eat",
    f"Wow, {favorite_food}, good choice."] 
# Choose one of those responses randomly
import random 
random_food_response = random.choice(list_of_food_responses)
# Print out one of those responses
print(random_food_response)