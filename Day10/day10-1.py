from pprint import pprint

# Import adapter data and generate myDevice rating
allAdapters = open('input.txt', 'r').read().splitlines()
allAdapters = [int(x) for x in allAdapters]
myDevice = max(allAdapters) + 3

# Add data for outlet and my device
allAdapters.append(myDevice)
allAdapters.append(0)

sortedAdapters = sorted(allAdapters)
pprint('All Adapters: ' + str(allAdapters))
pprint('Sorted Adapters: ' + str(sortedAdapters))
pprint('My Device: ' + str(myDevice))

single_jolt = 0
triple_jolt = 0
for i in range(1, len(sortedAdapters)):
	delta = sortedAdapters[i] - sortedAdapters[i-1]
	if delta == 1:
		single_jolt += 1
	elif delta == 3:
		triple_jolt += 1
pprint('Single Jolts: ' + str(single_jolt))
pprint('Triple Jolts: ' + str(triple_jolt))