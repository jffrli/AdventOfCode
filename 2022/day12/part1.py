with open("input.txt", "r") as f:
	data = [x.strip() for x in f.readlines()]

#initialize elevations
elevations = {'S':1,'E':26}
i = 1
for letter in 'abcdefghijklmnopqrstuvwxyz':
	elevations[letter] = i
	i += 1

for i in range(len(data)):
	if 'S' in data[i]:
		starty = i
		startx = data[i].index('S')
		break
	i += 1


dists = [[-1 for x in range(len(data[0]))] for y in range(len(data))]
dists[starty][startx] = 0
bfs = [(starty,startx)]

while len(bfs):
	nodey,nodex = bfs.pop(0)
	dist = dists[nodey][nodex]

	el  = elevations[data[nodey][nodex]]
	

	if data[nodey][nodex] == 'E':
		print(dist)
		break	
	
	if nodey-1 >= 0 and dists[nodey-1][nodex] == -1 and el - elevations[data[nodey-1][nodex]] >= -1:
		bfs.append((nodey-1,nodex))
		dists[nodey-1][nodex] = dist + 1

	if nodey+1 < len(data) and dists[nodey+1][nodex] == -1 and el - elevations[data[nodey+1][nodex]] >= -1:
		bfs.append((nodey+1,nodex))
		dists[nodey+1][nodex] = dist + 1

	if nodex-1 >= 0 and dists[nodey][nodex-1] == -1 and el - elevations[data[nodey][nodex-1]] >= -1:
		bfs.append((nodey,nodex-1))
		dists[nodey][nodex-1] = dist + 1

	if nodex+1 < len(data[0]) and dists[nodey][nodex+1] == -1 and el - elevations[data[nodey][nodex+1]] >= -1:
		bfs.append((nodey,nodex+1))
		dists[nodey][nodex+1] = dist + 1

