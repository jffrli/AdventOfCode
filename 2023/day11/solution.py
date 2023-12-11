import re
import sys

def getInput(filename: str = "input.txt"):
	with open(filename, "r") as f:
		data = f.read().strip().split("\n")
	return data


# thanks geeksforgeeks
# Python program to get transpose
# elements of two dimension list
def transpose(l1):

	# star operator will first
	# unpack the values of 2D list
	# and then zip function will 
	# pack them again in opposite manner
	l2 = [''.join(s) for s in zip(*l1)]
	return l2

def expansion(data:list, expand:int = 1):
	transposed = transpose(data)

	# find index to insert
	colsToInsert = []
	for x in range(len(transposed)):
		if transposed[x].find("#") == -1:
			colsToInsert.insert(0,x)
	rowsToInsert = []
	for x in range(len(data)):
		if data[x].find("#") == -1:
			rowsToInsert.insert(0,x)

	# # insert
	# for x in colsToInsert:
	# 	data = [row[:x] + "."*expand + row[x:] for row in data]
	# for x in rowsToInsert:
	# 	for i in range(expand):
	# 		data.insert(x,"." * len(data[0]))
	return rowsToInsert,colsToInsert

def findNodes(data, expand, expansionRows, expansionCols):
	nodes = []

	for r in range(len(data)):
		initialrownodes = [i for i,l in enumerate(data[r]) if l == "#"]
		rownodes = []
		for n in initialrownodes:
			empties = [e for e in expansionCols if e < n]
			j = -len(empties)
			rownodes.append(n + expand*len(empties) + j)

		if len(rownodes):
			empties = [e for e in expansionRows if e < r]
			j = -len(empties)
			nodes.extend([[r+len(empties)*expand+j,i] for i in rownodes])


	return nodes

def shortestPathAllPairs(nodes):

	# combination of all elements
	pairs = []
	for i in range(len(nodes)-1):
		for j in range(i+1,len(nodes)):
			pairs.append((nodes[i],nodes[j]))
	
	
	lengths = 0
	for a,b in pairs:
		lengths += abs(b[0]-a[0]) + abs(b[1]-a[1])

	return lengths

def solve(input, expand: int = 1):
	rta, cta = expansion(input,expand)

	nodes = findNodes(input,expand,rta,cta)
	if len(sys.argv) > 2:
		with open(sys.argv[2],"+a") as f:
			for n in nodes:
				f.write(str(n) + "\n")
			f.write("\n")
	pathsum = shortestPathAllPairs(nodes)
	return pathsum

def main():
	infile = "input.txt"
	if len(sys.argv) > 1:
		infile = sys.argv[1]
	input = getInput(infile)

	print("Part 1")
	print(solve(input))
	print()
	print("Part 2")
	# print(solve(input,10))
	# print(solve(input,100))
	print(solve(input,1000000))

if __name__ == '__main__':
	main()