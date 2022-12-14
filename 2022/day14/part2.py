from sys import exit

with open("input.txt", "r") as f:
	data = [[[int(z) for z in y.split(",")] for y in x.split("->")] for x in f.readlines()]


grid = [[0 for x in range(1000)] for y in range(170)]
source = [0,500]
grid[0][500] = 2

maxr = 0
#initialize rocks
for row in data:
	for i in range(1,len(row)):
		start = [row[i-1][1],row[i-1][0]]
		end = [row[i][1],row[i][0]]

		if start[0] > maxr:
			maxr = start[0]
		if end[0] > maxr:
			maxr = end[0]

		if start[0] == end[0]: #horizontal line
			for j in range(min(start[1],end[1]),max(start[1],end[1])+1):
				grid[start[0]][j] = 1
		else: #vertical line
			for j in range(min(start[0],end[0]),max(start[0],end[0])+1):
				grid[j][start[1]] = 1

grid[maxr+2] = [1 for x in range(1000)]


total = 0

while True:
	sy,sx = [source[0],source[1]] #generate new sand

	while True:
		if not grid[sy+1][sx]: #fall down
			sy += 1
		elif not grid[sy+1][sx-1]: #fall down+left
			sy += 1
			sx -= 1
		elif not grid[sy+1][sx+1]: #fall down+right
			sy += 1
			sx += 1
		else: #rest
			grid[sy][sx] = 3
			total += 1
			break

	if sy == source[0] and sx == source[1]:
		print(total)
		break


'''
for x in grid:
	print(''.join('.' if y == 0 else '#' if y == 1 else '+' if y == 2 else 'o' for y in x[400:]))
'''