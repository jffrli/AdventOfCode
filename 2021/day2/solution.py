
with open("input.txt", "r") as f:
	lines = f.readlines()



pos = 0
v1 = 0 #depth in part 1, aim in part 2
v2 = 0 #nothing in part 1, depth in part 2

for line in lines:
	x = line.split()
	if x[0] == "forward":
		pos += int(x[1])
		v2 += int(x[1]) * v1
	elif x[0] == "up":
		v1 -= int(x[1])
	elif x[0] == "down":
		v1 += int(x[1])

print(v1*pos)
print(v2*pos)