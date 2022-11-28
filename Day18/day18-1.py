def performCalculation(data, index):
	

line = '1 + 2 * 3 + 4 * 5 + 6'
data = line.split(' ')
print(data)

# Works w/o parentheses
result = int(data[0])
for i in range(len(data[1:])):
	if not data[i].isdigit():
		if data[i] == '+':
			result += int(data[i + 1])
		elif data[i] == '*':
			result *= int(data[i + 1])

print(result)