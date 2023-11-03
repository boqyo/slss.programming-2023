# author: shaun
# nov 3 2023
# world bot

total = 0

user_name = input("Hi whats your name? ")
print(f"Hi {user_name}")

continents = ["Asia ", "Europe", "North America ", "South America ", "Austrialia ", "Africa ", "Antarctica "]

for place in continents:
    visit = input(f"Have you been to {place}? ").lower().strip("!,'.?")
    if visit.lower().strip("!,.?") == "yes":
        total += 1


print(f"I see you've visited {total}/7 continents")
