import re

with open("input.txt","r") as f:
	data = [x.strip() for x in f.readlines()]

pattern = r'Valve (\w\w) [\w ]+=(\d+); [\w ]+valves? ((\w\w,? ?)+)'



flowrates = {}
state = {}
tunnels = {}

#setting the stage
for line in data:
	matches = re.match(pattern,line)
	valve = matches.group(1)
	state[valve] = 0
	flowrates[valve] = int(matches.group(2))
	tunnels[valve] = []

	for x in matches.group(3).split(", "):
		tunnels[valve].append(x)

dists = {}
#paths = {}

for x in tunnels.keys():
	dists[x] = {x:1}
	queue = [x]
	#paths[x] = {x:[]}
	while len(queue):
		node = queue.pop(0)
		for dest in tunnels[node]:
			if dest in dists[x]:
				continue
			queue.append(dest)
			dists[x][dest] = dists[x][node]+1
			#paths[x][dest] = paths[x][node].copy().append(dest)

# for k,v in dists.items():
# 	print(k)
# 	for a,b in v.items():
# 		print(a,b)
# 	print()

def getValue(flowrates,maxturns):
	values = [{} for x in range(maxturns)]
	for x in range(maxturns):
		for k,v in flowrates.items():
			values[x][k] = v*(maxturns-x)
	return values



def flowPotentials(dists,location,state,flowrates, turn, depth=1, maxturns = 30):
	potentials = {}
	if 0 not in state.values():
		return potentials
	for k,v in state.items():
		if v: #already on
			continue
		potentials[k] = (maxturns - turn - dists[location][k]) * flowrates[k]
		
		if depth and turn != maxturns: # search future potentials
			s = state.copy()
			s[k] = 1
			nextit = flowPotentials(dists,k,s,flowrates,turn+dists[location][k],depth-1)
			if len(nextit):
				potentials[k] += max(nextit.values())

	return potentials


def turnFlows(state,flowrates):
	flow = 0
	for k in state.keys():
		flow += state[k] * flowrates[k]
	return flow

flow = 0
location = 'AA'
t = 0
allon = False
while t < 30:
	flow += turnFlows(state,flowrates)
	if allon:
		t += 1
		continue

	pots = flowPotentials(dists,location,state,flowrates,t,2)
	if len(pots) == 0:
		allon = True
		t += 1
		continue
	greedy = max(pots, key=pots.get)
	#print(greedy)
	moves = dists[location][greedy]
	for i in range(moves):
		t += 1
		flow += turnFlows(state,flowrates)

	location = greedy
	state[location] = 1

	t += 1

print(flow)