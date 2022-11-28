startingNumbers = [0,3,6]

# Turn = index + 1
previousNumbers = []
gameNumbers = []
wordSpoken = None
debug = False
upperLimit = 30000000

for turn in range(1,upperLimit + 1):
	if turn < len(startingNumbers) + 1:
		wordSpoken = startingNumbers[turn - 1]
	else:
		if wordSpoken not in previousNumbers:
			wordSpoken = 0
		else:
			index1 = len(previousNumbers) - previousNumbers[::-1].index(wordSpoken) - 1
			index2 = len(previousNumbers)
			wordSpoken = index2 - index1
	previousNumbers = gameNumbers.copy()
	gameNumbers.append(wordSpoken)
	if debug:
		print('Turn: ' + str(turn))
		print('Previous Numbers: ' + str(previousNumbers))
		print('Work Spoken: ' + str(wordSpoken) + '\n')
	finalTurn = turn
print('The word spoken on turn ' + str(finalTurn) + ' is ' + str(gameNumbers[-1]))