# Author: Shaun
# Date: Oct 11 2023
# New years bot

import time

groceries = ["lego", "cake", "games", "stuff"]

# print it nicely

for item in groceries:
    print(f"* {item}")
    print(f" ---")

# make a * pyramid

pyramid = ["*", "**", "***", "****", "*****"]

for row in pyramid:
    print(row)

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "happy new years"]
for number in countdown:
    print(f"{number}")
    time.sleep(1)


    
