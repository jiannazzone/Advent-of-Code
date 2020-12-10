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

allOptions = []