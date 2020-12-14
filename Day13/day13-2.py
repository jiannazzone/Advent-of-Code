from pprint import pprint

# Import data
data = open('sample.txt', 'r').read().splitlines()
busses = data[1].split(',')
busses = [int(x) if x != 'x' else 'x' for x in busses]
print(busses)

offsetDictionary = {}
for i in range(len(busses)):
	if busses[i] == 'x':
		offsetDictionary[i+1] = None
	else:
		offsetDictionary[i+1] = int(busses[i])
