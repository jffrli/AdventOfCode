with open("input.txt","r") as f:
    lines = f.readlines()

plays = [x.split() for x in lines]


score = 0

for o,s in plays:
    if s == "X":
        if o == "A":
            score += 3
        elif o == "B":
            score += 1
        elif o == "C":
            score += 2
    elif s == "Y":
        score += 3
        if o == "A":
            score += 1
        elif o == "B":
            score += 2
        elif o == "C":
            score += 3
    elif s == "Z":
        score += 6
        if o == "A":
            score += 2
        elif o == "B":
            score += 3
        elif o == "C":
            score += 1

print(score)