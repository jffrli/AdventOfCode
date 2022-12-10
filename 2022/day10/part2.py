with open("input.txt", "r") as f:
	data = [x.strip().split() for x in f.readlines()]

cycle = 0
regX = 1


out = [[]]

for instruction in data:
	if len(out[-1]) >= 40:
		out.append([])
	if (regX-1 <= cycle%40 and regX+1 >= cycle%40) or (regX-1 >= cycle and (regX+1)%40 <= cycle%40):
		out[-1].append("#")
	else:
		out[-1].append(".")

	if instruction[0] == "addx":
		cycle += 1
		if len(out[-1]) >= 40:
			out.append([])
		if (regX-1 <= cycle and regX+1 >= cycle%40) or (regX-1 >= cycle and (regX+1)%40 <= cycle%40):
			out[-1].append("#")
		else:
			out[-1].append(".")

		regX += int(instruction[1])
	cycle += 1 

for line in out:
	print(''.join(line))