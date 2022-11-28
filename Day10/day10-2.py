from pprint import pprint
from collections import Counter

def cheater(jolts):
	dp = Counter()
	dp[0] = 1

	for jolt in jolts:
	    # print(f"Count of {jolt} = {dp[jolt-1]} + {dp[jolt-2]} + {dp[jolt-3]}")
	    dp[jolt] = dp[jolt-1] + dp[jolt-2] + dp[jolt-3]

	print(dp[jolts[-1]])

# Import adapter data and generate myDevice rating
allAdapters = open('input.txt', 'r').read().splitlines()
allAdapters = [int(x) for x in allAdapters]
myDevice = max(allAdapters) + 3

# Add data for outlet and my device
# allAdapters.append(myDevice)
# allAdapters.append(0)

sortedAdapters = sorted(allAdapters)
# pprint('All Adapters: ' + str(allAdapters))
pprint('Sorted Adapters: ' + str(sortedAdapters))

cheater(sortedAdapters)