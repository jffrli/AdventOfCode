def getScene(x,y,data):
	target = data[y][x]
	l = 0
	r = 0
	u = 0
	d = 0
	# left
	a = x-1
	b = y
	while a >= 0:
		l += 1
		if data[b][a] >= target:
			break
		a -= 1

	# right
	a = x+1
	b = y
	while a < len(data[y]):
		r += 1
		if data[b][a] >= target:
			break
		a += 1

	# up
	a = x
	b = y-1
	while b >= 0:
		u += 1
		if data[b][a] >= target:
			break
		b -= 1

	# down
	a = x
	b = y+1
	while b < len(data):
		d += 1
		if data[b][a] >= target:
			break
		b += 1	

	return l*r*u*d

with open("input.txt", "r") as f:
	data = [x.strip() for x in f.readlines()]

high = 0
for a in range(1,len(data)-1):
	for b in range(1,len(data[0])-1):
		x = getScene(a,b,data)
		if x > high:
			high = x

print(high)


