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

data.append([2])
data.append([6])

from functools import cmp_to_key
data = sorted(data, key=cmp_to_key(compare), reverse=True)

print((data.index([2])+1) * (data.index([6])+1))
