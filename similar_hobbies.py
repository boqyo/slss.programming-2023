# Author shuaun
# nov 15 2023


print("Please enter hobbies seperated by commas and a space.")
# Get person 1 hobby
hobby_one = input("Person 1: ").lower().split(", ")

# Get person 2 hobby
hobby_two = input("Person 2: ").lower().split(", ")

# FInd in common
hobby_same = 0
for hobbies in hobby_one:
    if hobbies in hobby_two:
        hobby_same += 1

print(f"You have {hobby_same} hobbies in common.")