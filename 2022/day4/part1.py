with open("input.txt", "r") as f:
	lines = [x.strip() for x in f.readlines()]

pairs = [[y.split('-') for y in x.split(',')] for x in lines]

count = 0
for a,b in pairs:
	x = [int(i) for i in a]
	y = [int(j) for j in b]
	x.sort()
	y.sort()

	if (x[0] <= y[0] and x[1] >= y[1]) or \
		(y[0] <= x[0] and y[1] >= x[1]):
		count += 1

print(count)