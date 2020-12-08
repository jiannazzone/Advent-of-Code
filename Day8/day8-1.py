from pprint import pprint

rawInstructions = open('input.txt', 'r').read().splitlines()
instructions = []
for i in rawInstructions:
	a = str(i[:3])
	b = int(i[4:])
	instructions.append((a, b))

accumulator = 0
j = 0

alreadyRun = []

while True:
	thisInstruction = instructions[j][0]
	thisValue = instructions[j][1]
	if j in alreadyRun:
		print(accumulator)
		break
	alreadyRun.append(j)
	if thisInstruction == 'acc':
		accumulator += thisValue
		j += 1
	elif thisInstruction == 'jmp':
		j += thisValue
	else:
		j += 1