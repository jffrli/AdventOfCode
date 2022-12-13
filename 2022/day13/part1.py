def compare(left, right):
	if isinstance(left,list) or isinstance(right,list):
		if not isinstance(left,list):
			left = [left]
		if not isinstance(right,list):
			right = [right]

		if len(left) > len(right):
			return False
		
		for i in range(len(left)):
			if i >= len(right):
				return False
			if not compare(left[i],right[i]):
				return False
		return True
	else:
		return left <= right

with open("input.txt", "r") as f:
	data = [eval(x.strip()) for x in f.readlines() if x.strip()]

total = 0
for i in range(0,len(data),2):

	if compare(data[i], data[i+1]):
		total += 1 + int(i/2)

print(total)