def compare(left, right):
	if isinstance(left,list) or isinstance(right,list):
		if not isinstance(left,list):
			left = [left]
		if not isinstance(right,list):
			right = [right]		
		for i in range(len(left)):
			if i >= len(right): #right side runs out first
				return -1
			res = compare(left[i],right[i])
			if res == 1:
				return 1
			elif res == -1:
				return -1

		if len(left) < len(right):
			return 1
		else:
			return 0
	else:
		if left < right:
			return 1
		if right < left:
			return -1
		return 0

with open("input.txt", "r") as f:
	data = [eval(x.strip()) for x in f.readlines() if x.strip()]

total = 0
for i in range(0,len(data),2):

	if compare(data[i], data[i+1]) == 1:
		total += 1 + int(i/2)

print(total)