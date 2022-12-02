with open("input.txt", "r") as f:
    cals = f.read()
elves = cals.split("\n\n")
#print(len(elves))
ecs = []
for elf in elves:
    ec = [int(x) for x in elf.split("\n")]
    ecs.append(sum(ec))

list.sort(ecs)
print(ecs[-1]) #part 1
print(sum(ecs[-3:])) #part 2