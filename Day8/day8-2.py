from pprint import pprint

rawInstructions = open('sample.txt', 'r').read().splitlines()
instructions = []
for i in rawInstructions:
	a = str(i[:3])
	b = int(i[4:])
	instructions.append([a, b])

accumulator = 0
j = 0
alreadyRun = []

while j < len(instructions):
	thisInstruction = instructions[j][0]
	thisValue = instructions[j][1]
	if j in alreadyRun:
		if instructions[j][0] == 'nop':
			instructions[j][0] = 'jmp'
		else:
			instructions[j][0] = 'nop'
	alreadyRun.append(j)
	if thisInstruction == 'acc':
		accumulator += thisValue
		j += 1
	elif thisInstruction == 'jmp':
		j += thisValue
	else:
		j += 1

j = 0
while j < len(instructions):
	thisInstruction = instructions[j][0]
	thisValue = instructions[j][1]
	if thisInstruction == 'acc':
		accumulator += thisValue
		j += 1
	elif thisInstruction == 'jmp':
		j += thisValue
	else:
		j += 1
print(accumulator)