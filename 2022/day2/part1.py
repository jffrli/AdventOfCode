with open("input.txt","r") as f:
    lines = f.readlines()

plays = [x.split() for x in lines]


score = 0

for o,s in plays:
    if s == "X":
        score += 1
        if o == "A":
            score += 3
        elif o == "C":
            score += 6
    elif s == "Y":
        score += 2
        if o == "B":
            score += 3
        elif o == "A":
            score += 6
    elif s == "Z":
        score += 3
        if o == "C":
            score += 3
        elif o == "B":
            score += 6

print(score)