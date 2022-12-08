with open("input.txt", "r") as f:
	data = [x.strip() for x in f.readlines()]

visible = [[0 for x in data[0]] for y in data]

# Initialize visible
visible[0] = [1 for x in data[0]]
visible[-1] = [1 for x in data[0]]
for a in range(1,len(visible)-1):
	visible[a][0] = 1
	visible[a][-1] = 1

for a in range(1,len(data)-1):
	left = data[a][0]
	right = data[a][-1]

	for b in range(1,len(data[0])-1):
		if data[a][b] > left:
			left = data[a][b]
			visible[a][b] = 1
		if data[a][-(1+b)] > right:
			right = data[a][-(1+b)]
			visible[a][-(1+b)] = 1


for a in range(1,len(data[0])-1):
	up = data[0][a]
	down = data[-1][a]

	for b in range(1,len(data)-1):
		if data[b][a] > up:
			up = data[b][a]
			visible[b][a] = 1
		if data[-(1+b)][a] > down:
			down = data[-(1+b)][a]
			visible[-(1+b)][a] = 1


count = 0
for x in visible:
	#print(x)
	for y in x:
		if y == 1:
			count += 1

print(count)