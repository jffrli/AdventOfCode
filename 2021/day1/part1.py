with open("input","r") as f:
    lines = f.readlines()

measurements = [int(x) for x in lines]

ma = measurements[:-1]
mb = measurements[1:]

count = 0

for a,b in zip(ma,mb):
    count += (b - a > 0)

print(count)