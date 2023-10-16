#Author: Shaun HA
#Date: October 16
#Star wars bot
#Introduce bot
import time
print("I am going to decide if you're part of the light side or the dark side")
time.sleep(1)
#Ask user colour and cape
colour = input("Is red your favorite colour? ")
time.sleep(1)
if colour.lower().strip("!,.") == "yes":
    dark_cape = input("Do you like capes? ")

time.sleep(1)
if colour.lower().strip("!,.") == "no":
     dark_cape = input("Do you like capes? ")
     
#Make outcome depending on the two answers
if colour.lower().strip("!,.") == "yes" or dark_cape.lower().strip("!,.") =="yes":
     print("Dark side I see..")

if colour.lower().strip("!,.") == "no" and dark_cape.lower().strip("!,.") =="no":
     print("Light side I see..")