import math

def getInput(filename = "input.txt"):
    with open(filename,"r") as f:
        filedata = f.readlines()
    
    instructions = filedata[0].strip()
    locationdata = filedata[2:]

    locations = {}
    for location in locationdata:
        x = location.split(" = ")
        locations[x[0]] = x[1][1:-2].split(", ")

    return instructions,locations

instructions, locations = getInput()

def solution(instructions,locations):

    curr = [x for x in locations.keys() if x[-1] == "A"]
    
    ste = 1

    for x in curr:
        steps = 0
        # print(x)
        while not x[-1] == "Z":
            x = locations[x][0] if instructions[steps % len(instructions)] == "L" else locations[x][1]
            # print(x + ": " + str(steps % len(instructions)) + " " + instructions[steps % len(instructions)])
            steps += 1
        # print(x)
        # print(steps)
        ste = math.lcm(ste,steps)


    return ste


print(solution(instructions,locations))