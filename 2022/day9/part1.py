def follow(head,tail):
	if abs(head[1]-tail[1]) > 1 and head[0] == tail[0]:
		if head[1] > tail[1]:
			tail[1] += 1
		else:
			tail[1] -= 1
	elif abs(head[0]-tail[0]) > 1 and head[1] == tail[1]:
		if head[0] > tail[0]:
			tail[0] += 1
		else:
			tail[0] -= 1
	elif abs(head[1]-tail[1]) > 1 or abs(head[0]-tail[0]) > 1: # move diagonal
		if head[0] > tail[0]:
			tail[0] += 1
		else:
			tail[0] -= 1
		if head[1] > tail[1]:
			tail[1] += 1
		else:
			tail[1] -= 1


with open("input.txt", "r") as f:
	data = [x.strip().split() for x in f.readlines()]

visited = set()

head = [0,0]
tail = [0,0]

for action in data:
	di = action[0]
	if di == "R":
		dx = 1
		dy = 0
	elif di == "L":
		dx = -1
		dy =0 
	elif di == "U":
		dy = 1
		dx = 0
	else:
		dy = -1
		dx = 0

	for i in range(int(action[1])):
		head[0] += dx
		head[1] += dy

		follow(head,tail)
		visited.add(tuple(tail))

print(len(visited))
