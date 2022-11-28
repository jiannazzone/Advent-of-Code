from pprint import pprint

def getMaskedAddress(address, mask):
	maskedAddress = ''
	for i in range(36):
		if mask[i] == '0':
			maskedAddress += address[i]
		elif mask[i] == '1':
			maskedAddress += '1'
		else:
			maskedAddress += 'X'
	return maskedAddress
def branchAddress(address, possibleAddresses):
	firstX = address.find('X')
	if firstX != -1:
		a = address[:firstX] + '0' + address[firstX + 1:]
		branchAddress(a, possibleAddresses)
		b = address[:firstX] + '1' + address[firstX + 1:]
		branchAddress(b, possibleAddresses)
	else:
		possibleAddresses.append(int(address, 2))

# Import and clean data
rawData = open('input.txt', 'r').read().split('mask = ')
rawData.pop(0)
rawData = [x.replace('mem[', '') for x in rawData]
rawData = [x.replace('] = ', ':') for x in rawData]

# Dictionary representing memory addresses and their values
memoryBank = {}

# Organize into a list, where each entry is a list with:
# The mask as a string, and
# A list of tuples (address, number)
commands = []
for i in rawData:
	thisMask = i.splitlines()[0]
	theseLists = []
	for x in i.splitlines()[1:]:
		a = int(x[:x.index(':')])
		address = f'{a:036b}'
		value = int(x[x.index(':')+1:])
		theseLists.append([address, value])
	commands.append([thisMask, theseLists])

# Uncomment the line below to see structure more clearly
# pprint(commands[0:3])

# Iterate through each group of mask plus its addresses/values
for i in range(len(commands)):
	thisMask = commands[i][0]

	# Apply the mask to all associated addresses, one-by-one
	for j in range(len(commands[i][1])):
		maskedAddress = getMaskedAddress(commands[i][1][j][0], thisMask)

		# For each masked addresses, generate a list of
		# All applicable memory addresses
		possibleAddresses = []
		branchAddress(maskedAddress, possibleAddresses)

		# Write value to each of those memory addresses
		for h in possibleAddresses:
			memoryBank[h] = commands[i][1][j][1]

# Generate sum of all memory values
total = 0
for i in memoryBank.keys():
	total += memoryBank[i]
print('Memory Bank Total: ' + str(total))