# Author: shaun
# Nov 3 2023
# Semester

total_rating = 0

course_amount = int(input(f"How many courses are you taking? "))

for i in range(course_amount):
    rating = int(input(f"How do you rate course {i + 1}? "))
    total_rating += rating

average = total_rating / course_amount

if average <= 1:
    print(average, "Ouch.")

if average > 1 and average <= 3:
    print(average, "Not bad.")

if average > 3 and average <= 5:
    print(average ,"Glad to hear")