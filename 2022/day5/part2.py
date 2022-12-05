with open("input.txt", "r") as f:
	d = f.read()

data = d.split("\n\n")

s = data[0].split("\n")
stacks = {}

for x in s[-1].split():
	stacks[int(x)] = []

for i in range(len(s)-1):
	line = s[-(2+i)]
	k = 1
	for j in range(1,len(line),4):
		if line[j] != " ":
			stacks[k].append(line[j])
		k += 1

instructs = data[1].split("\n")
instructions = [x.split(" ") for x in instructs]

for x in instructions:

	temp = []
	for i in range(int(x[1])):
		temp.append(stacks[int(x[3])].pop())
	for i in range(int(x[1])):
		stacks[int(x[5])].append(temp.pop())


message = [" " for x in stacks]

for k,v in stacks.items():
	message[k-1] = v[-1]

print(''.join(message))


