# Turtle example
# Author: me
# 22 nov 2023

import turtle

# make turtle that can move around screen
FORWARD_MAGNITUDE = 20

# make tutrle object
micheal = turtle.Turtle()

# Get input from user
print("""To give commands, type:
F to go forwards
L to turn left
R to turn right""")

done = False
while not done:
    command = input("Where should I go ")


# move turltle

    if command.strip("!,.?").lower() == "f":
        micheal.forward(FORWARD_MAGNITUDE)
    elif command.strip("!,.?").lower() == "l":
        micheal.left(90)
    elif command.strip("!,.?").lower() == "r":
        micheal.right(90)

done = True


