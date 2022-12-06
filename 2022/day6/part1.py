with open("input.txt","r") as f:
	message = f.read()

start = message[:3]

for i in range(3,len(message)):
	x = message[i]
	if len(set(start)) == 3 and x not in start:
		print(i+1)
		break
	start = start[1:] + x
