with open("input.txt", "r") as f:
	data = [x.strip().split() for x in f.readlines()]

cycle = 1
regX = 1

total = 0

for instruction in data:
	if cycle % 40 == 20:
			total += cycle * regX
	if instruction[0] == "addx":
		cycle += 1
		if cycle % 40 == 20:
			total += cycle * regX
		regX += int(instruction[1])
	cycle += 1


print(total)