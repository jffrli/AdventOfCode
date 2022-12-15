import re

def mdist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def levelLimits(mdist,sensor, lowy = 0, highy = 4000000):
	#mdist >= abs(sensor[1] - level)
	y1 = mdist + sensor[1]
	y2 = sensor[1] - mdist
	low = min(y1,y2)
	high = max(y1,y2)
	if low > highy or high < lowy:
		return False
	return [max(low,lowy),min(high,highy)]


def disallowRange(mdist, sensor, level, lowx = 0, highx = 4000000):
	vertdist = abs(sensor[1] - level)
	if mdist < vertdist: #unsolvable
		return False

	x1 = sensor[0] - (mdist - vertdist)
	x2 = sensor[0] + (mdist - vertdist)
	low = min(x1,x2)
	high = max(x1,x2)
	if low > highx or high < lowx: #outside the range we care about
		return False
	return [max(low,lowx),min(high,highx)]

with open("input.txt","r") as f:
	data = [x.strip() for x in f.readlines()]

grid = [[] for y in range(4000001)]

reg = r'[a-zA-Z\s=:,\b]+(-?\d+)[a-zA-Z\s=:,\b]+(-?\d+)[a-zA-Z\s=:,\b]+(-?\d+)[a-zA-Z\s=:,\b]+(-?\d+)'


for line in data:
	if not len(line):
		break
	d = re.match(reg,line)

	#print(d.group(1),d.group(2),d.group(3),d.group(4))
	sensor = [int(d.group(1)),int(d.group(2))]
	beacon = [int(d.group(3)),int(d.group(4))]

	closest = mdist(sensor, beacon)

	levels = levelLimits(closest, sensor)
	if levels:
		for level in range(levels[0],levels[1]+1):
			xs = disallowRange(closest,sensor,level)
			if xs:
				grid[level].append(xs)

def collapseRanges(ranges):
	alldone = False
	while True:
		poplist = set()
		for i in range(len(ranges)):
			for j in range(i+1,len(ranges)):
				if ranges[i][0] <= ranges[j][0] and ranges[i][1] >= ranges[j][0]:
					poplist.add(j)
					alldone = False
					ranges[i][1] = max(ranges[i][1],ranges[j][1])

				if ranges[i][0] <= ranges[j][1] and ranges[i][1] >= ranges[j][1]:
					poplist.add(j)
					alldone = False
					ranges[i][0] = min(ranges[i][0],ranges[j][0])
		if len(poplist) == 0:
			if alldone:
				break
			alldone = True
			continue
		for x in sorted(poplist, reverse=True):
			ranges.pop(x)

for y in range(len(grid)):
	row = grid[y]
	if [0,4000000] in row:
		continue

	collapseRanges(row)

	if [0,4000000] not in row:
		#print(row)
		rset = set()
		for r in row:
			rset.update(range(r[0],r[1]+1))
		allnums = set(range(0,4000001))
		x = allnums.difference(rset).pop()
		print(x*4000000+y)
		break

