from pprint import pprint

def branchAddress(address):
	firstX = address.find('X')
	if firstX != -1:
		a = address[:firstX] + '0' + address[firstX + 1:]
		branchAddress(a)
		b = address[:firstX] + '1' + address[firstX + 1:]
		branchAddress(b)
	else:
		possibleBinary.append(address)

mask = '000000000000000000000000000000X1001X'
address = 42
value = 100

addressInBinary = f'{address:036b}'
maskedAddress = ''

for i in range(36):
	if mask[i] == '0':
		maskedAddress += addressInBinary[i]
	elif mask[i] == '1':
		maskedAddress += '1'
	else:
		maskedAddress += 'X'

global possibleBinary
possibleBinary = []
branchAddress(maskedAddress)
pprint(possibleBinary)