from pprint import pprint

startingNumbers = [8,0,17,4,1,12]
lastSpoken = {}

finalTurn = 30000000
nextNum = 0

for turn in range(1, finalTurn + 1):
	lastNum = nextNum

	# Create initial dictionary
	if turn < len(startingNumbers):
		lastSpoken[startingNumbers[turn - 1]] = turn
		nextNum = startingNumbers[turn]
	else:
		if lastNum not in lastSpoken:
			nextNum = 0
		else:
			nextNum = turn - lastSpoken[lastNum]

		lastSpoken[lastNum] = turn
	finalTurn = turn

print('Turn ' + str(finalTurn) + ': ' + str(lastNum))