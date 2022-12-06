with open("input.txt","r") as f:
	message = f.read()

start = message[:13]

for i in range(3,len(message)):
	x = message[i]
	if len(set(start)) == 13 and x not in start:
		print(i+1)
		break
	start = start[1:] + x
