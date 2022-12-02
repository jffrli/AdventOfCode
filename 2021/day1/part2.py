with open("input","r") as f:
    lines = f.readlines()

measurements = [int(x) for x in lines]

ma = measurements[:-2]
mb = measurements[1:-1]
mc = measurements[2:]

count = 0
prev = 0
for a,b,c in zip(ma,mb, mc):
    curr = a+b+c
    if prev:
        count += (curr - prev > 0)
    prev = curr

print(count)