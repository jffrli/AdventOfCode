with open("input.txt", "r") as f:
	lines = [x.strip() for x in f.readlines()]

groups = []
group = []


for line in lines:
	group.append(line)
	if len(group) >= 3:
		groups.append(group)
		group = []


priorities = 0

for g in groups:
	found = False
	
	for a in g[0]:
		if a in g[1] and a in g[2]:

			if a.isupper():
				priorities += 27 + ord(a)-ord('A')
			else:
				priorities += 1 + ord(a)-ord('a')

			break

print(priorities)