with open("input.txt","r") as f:
	lines = [x.strip() for x in f.readlines()]


ovals = lines.copy()
ograting = []
for i in range(len(ovals[0])):
	digit = [int(x[i]) for x in ovals]
	common = int(sum(digit) >= len(ovals)/2)

	newvals = []
	for x in ovals:
		if int(x[i]) == common:
			newvals.append(x)

	ovals = newvals.copy()

	if len(ovals) == 1:
		ograting = ovals[0]
		break

cvals = lines.copy()
corating = []
for i in range(len(cvals[0])):
	digit = [int(x[i]) for x in cvals]
	common = int(sum(digit) >= len(cvals)/2)

	newvals = []
	for x in cvals:
		if int(x[i]) != common:
			newvals.append(x)
	cvals = newvals.copy()

	if len(cvals) == 1:
		corating = cvals[0]
		break

print(int(''.join(map(str,ograting)),2)*int( ''.join(map(str,corating)) ,2))