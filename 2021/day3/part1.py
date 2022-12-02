with open("input.txt","r") as f:
	lines = [x.strip() for x in f.readlines()]

counts = [0 for x in lines[0]]

for line in lines:
	for i in range(len(counts)):
		counts[i] += int(line[i])

gamma = [int(x >= len(lines)/2) for x in counts]
epsilon = [int(x == 0) for x in gamma]


print(int(''.join(map(str,gamma)),2)*int( ''.join(map(str,epsilon)) ,2))