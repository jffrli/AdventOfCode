with open("input.txt", "r") as f:
	terminal = [x.split() for x in f.readlines()]

sizes = {}
path = []

for cmd in terminal:

	if cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] != '..':
		
		path.append(cmd[2])
		sizes[''.join(path)] = 0
	elif cmd[0] == '$' and cmd[1] == 'cd': # must be ..
		path.pop()
	elif cmd[0] != '$' and cmd[0] != 'dir':
		sizes[''.join(path)] += int(cmd[0])
		for x in range(1,len(path)-1):
			sizes[''.join(path[:-x])] += int(cmd[0])

total = 0
for dire, size in sizes.items():
	if size <= 100000:
		total += size

print(total)