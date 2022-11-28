from pprint import pprint

# Import data
data = open('input.txt', 'r').read().splitlines()
timestamp = int(data[0])
busses = data[1].split(',')
runningBusses = [int(x) for x in busses if x != 'x']

waitTimes = {}
for i in runningBusses:
	thisWait = i - (timestamp % i)
	waitTimes[i] = thisWait

bestBus = min(waitTimes, key = waitTimes.get)
finalWait = waitTimes[bestBus]

print('Bus: ' + str(bestBus))
print('Wait Time: ' + str(finalWait))
print('Product: ' + str(bestBus*finalWait))