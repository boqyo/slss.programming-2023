# Author: Shaun ha
# date november 1 2023
# judge score

final_score = 0

judge_score = ["Judge 1: ", "Judge 2: ", "Judge 3: ", "Judge 4: ", "Judge 5: "]

for judge in judge_score:
    print(judge)
    score = float(input().strip("!,.?"))
    if score < 0 or score > 10:
        break
    else:
        final_score += score

print({round ((final_score / 5), 2)})
