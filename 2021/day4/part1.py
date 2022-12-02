def checkbingo(mark):
	#print()
	for i in range(5):
		#print(mark[i])
		#print([x[i] for x in mark])
		if not sum(mark[i]) or not sum([x[i] for x in mark]):
			return True
	return False

def markboard(board,mark, target):
	tar = int(target)
	for i in range(5):
		for j in range(5):
			if board[i][j] == tar:
				mark[i][j] = 0

def getscore(board, mark, lastcall):
	count = 0
	for i in range(5):
		for j in range(5):
			count += board[i][j] * mark[i][j]

	return count*int(lastcall)

with open("input.txt", "r") as f:
	lines = f.read()

data = lines.split("\n\n")

calls = data[0].split(",")
boards = [[list(map(int,y.split())) for y in x.split("\n")] for x in data[1:]]

#print(boards[-1])
marks = [[[1,1,1,1,1] for y in range(5)] for x in range(len(boards))]

for call in calls:
	for i in range(len(boards)):
		board = boards[i]
		mark = marks[i]

		markboard(board,mark,call)
		if checkbingo(mark):
			print(getscore(board,mark,call))
			exit()
