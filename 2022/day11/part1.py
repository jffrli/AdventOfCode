def inspection(monkey, num, inventories, inspects):
	operation = monkey[2].split("=")[1].split()
	
	test = int(monkey[-3].split()[-1])

	#print(monkey[-1].split())
	tm = int(monkey[-2].split()[-1])
	fm = int(monkey[-1].split()[-1])

	if operation[1] == "*":
		if  operation[2] == "old":
			op = lambda x : x * x
		else:
			op = lambda x : x * int(operation[2])
	else:
		if  operation[2] == "old":
			op = lambda x : x + x
		else:
			op = lambda x : x + int(operation[2])

	while len(inventories[num]):
		item = inventories[num].pop()
		inspects[num] += 1

		newitem = op(item)//3

		if not newitem%test:
			inventories[tm].append(newitem)
		else:
			inventories[fm].append(newitem)


with open("input.txt", "r") as f:
	data = f.read().split("\n\n")

monkeys = [[y for y in x.split("\n") if y] for x in data]

inventories = [[] for x in range(len(monkeys))]
inspects = [0 for x in range(len(monkeys))]
#initiate
for i in range(len(monkeys)):
	monkey = monkeys[i]
	items = monkey[1].split(":")[1].split(", ")
	inventories[i] = [int(x) for x in items]

#20 rounds
for r in range(20):
	for i in range(len(monkeys)):
		inspection(monkeys[i],i,inventories,inspects)
		

inspects.sort()
print(inspects[-1]*inspects[-2])