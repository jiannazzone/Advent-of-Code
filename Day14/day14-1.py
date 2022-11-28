from pprint import pprint

# Import and clean data
rawData = open('input.txt', 'r').read().split('mask = ')
rawData.pop(0)
rawData = [x.replace('mem[', '') for x in rawData]
rawData = [x.replace('] = ', ':') for x in rawData]

# Organize into a list, where each entry is a list with:
# The mask as a string, and
# A list of tuples (address, number)
commands = []
for i in rawData:
	thisMask = i.splitlines()[0]
	theseTuples = []
	for x in i.splitlines()[1:]:
		theseTuples.append(
			(int(x[:x.index(':')]), int(x[x.index(':')+1:]))
			)
	commands.append([thisMask, theseTuples])

# Create dictionary of all relevant memory addresses
memoryDictionary = {}
for x in commands:
	for y in x[1]:
		memoryDictionary[y[0]] = f'{0:036b}'

for x in commands:
	thisMask = x[0] # This mask
	# print('Mask: ' + thisMask)
	for y in x[1]: # x[1] = All commands for this mask
		thisBinary = f'{y[1]:036b}' # Number as binary string
		newValue = ''
		for z in range(36):
			if thisMask[z] == 'X':
				newValue += thisBinary[z]
			else:
				newValue += thisMask[z]
		memoryDictionary[y[0]] = newValue
		# print('Address: ' + str(thisAddress))
		# print('Address Previously: ' + str(addressOld))
		# print('Value: ' + str(thisBinary))

sum = 0
for key in memoryDictionary.keys():
	sum += int(memoryDictionary[key], 2)
print(sum)