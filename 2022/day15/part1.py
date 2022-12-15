import re

def mdist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def disallowRange(mdist, sensor, level = 2000000):
	vertdist = abs(sensor[1] - level)
	if mdist < vertdist: #unsolvable
		return False

	x1 = sensor[0] - (mdist - vertdist)
	x2 = sensor[0] + (mdist - vertdist)
	return [min(x1,x2),max(x1,x2)]

with open("input.txt","r") as f:
	data = [x.strip() for x in f.readlines()]

#grid = [[0 for y in range(10000000)] for x in range(10000000)]

reg = r'[a-zA-Z\s=:,\b]+(-?\d+)[a-zA-Z\s=:,\b]+(-?\d+)[a-zA-Z\s=:,\b]+(-?\d+)[a-zA-Z\s=:,\b]+(-?\d+)'

disallowed = set()

for line in data:
	if not len(line):
		break
	d = re.match(reg,line)

	#print(d.group(1),d.group(2),d.group(3),d.group(4))
	sensor = [int(d.group(1)),int(d.group(2))]
	beacon = [int(d.group(3)),int(d.group(4))]

	closest = mdist(sensor, beacon)
	
	dr = disallowRange(closest, sensor, 2000000)
	if dr:
		disallowed.update(range(dr[0],dr[1]))
		#disallowed.update(range(dr[0],dr[1]+1)) #(not sure why this doesn't work)

print(len(disallowed))