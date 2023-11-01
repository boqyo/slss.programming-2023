final_score = 0

judge_score = ["Judge 1: ", "Judge 2: ", "Judge 3: ", "Judge 4: ", "Judge 5: "]

for judge in judge_score:
    print(judge)
    score = int(input().strip("!,.?"))
    final_score += score



if score < 0 or score > 10:
    

print(final_score) / 5
