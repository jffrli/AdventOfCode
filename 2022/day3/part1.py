with open("input.txt", "r") as f:
	lines = [x.strip() for x in f.readlines()]

priorities = 0

for line in lines:
	half = int(len(line)/2)

	a = line[:half]
	b = line[half:]

	found = False
	for x in a:
		
		for y in b:
			if x == y:

				found = True


				if x.isupper():

					priorities += 27 + ord(x)-ord('A')
				else:

					priorities += 1 + ord(x)-ord('a')
				break

		if found:
			break

print(priorities)
