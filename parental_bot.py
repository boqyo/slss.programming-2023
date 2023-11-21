# Author: Shaun
# Date nov 21 2023


questions = [
    "Did you eat ", 
    "Did you study? ", 
    "Did you do laundry? ", 
    "Did you call grandma? "
]


good = 0
for questions in questions:
    answer = input(questions)
    if answer.lower().strip(",.!?") == "yes":
        good += 1


if good <= 0:
    print("Im coming over")

if good >= 1 and good <= 2:
    print("Ok")

if good >= 3 and good <= 4:
    print("Good")