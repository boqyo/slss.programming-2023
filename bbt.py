# Bubble tea popularity
# Author : Shaun
# Oct 27 20223

# ask 5 users what their favourite bubble tea place is
# prints summary of data

# number of voters

NUM_RESPONDENTS = 7

# ------

coco_likes = 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    print("Whats your favorite bubble tea")
    fave_place = input().strip("!,.?").lower()

# Tally or counting sign

    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1       # alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1

print(f"CoCo Likes: {coco_likes}")
print(f"Suntea Likes: {suntea_likes}")
print(f"chatime Likes: {chatime_likes}")
print(f"bubble queen Likes: {bubqueen_likes}")

coco_percentage = coco_likes / 7 * 100
suntea_percentage = suntea_likes / 7 * 100
chatime_percentage = chatime_likes / 7 * 100
bubqueen_percentage = bubqueen_likes / 7 * 100


print(f"Coco vote percentage: {round(coco_percentage, 2)}%")
print(f"Suntea vote percentage: {round(suntea_percentage, 2)}%")
print(f"chatime vote percentage: {round(chatime_percentage, 2)}%")
print(f"bubble queen vote percentage: {round(bubqueen_percentage, 2)}%")

