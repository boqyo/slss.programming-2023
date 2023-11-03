total = 0

user_name = input("Hi, what's your name? ")
print(f"Hi {user_name}")

continents = ["Asia", "North America", "South America", "Australia", "Africa", "Antarctica"]

for place in continents:
    visit = input(f"Have you been to {place}? ").strip("!,'.?, ").lower()
    if visit == "yes":
        total += 1

print(f"I see you've visited {total}/6 continents")