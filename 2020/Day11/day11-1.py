# Day 11-1
from pprint import pprint

def checkRowAndCol(row, col):
	isTop = isRight = isBottom = isLeft = False
	# Check if top row
	if row == 0:
		isTop = True

	# Check if right column
	if col == totalCounts[1] - 1:
		isRight = True

	# Check if bottom row
	if row == totalCounts[0] - 1:
		isBottom = True

	# Check if left column
	if col == 0:
		isLeft = True

	return (isTop, isRight, isBottom, isLeft)
def checkAbove(row, col, previousState):
	thisCount = 0
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)

	if not isLeft: # Account for left column edge case
		if previousState[row - 1][col - 1] == '#':
			thisCount += 1 # Top Left

	if previousState[row - 1][col] == '#':
		thisCount += 1 # Top Middle

	if not isRight: # Account for right column edge case
		if previousState[row - 1][col + 1] == '#':
			thisCount += 1 # Top Right

	return(thisCount)
def checkSides(row, col, previousState):
	thisCount = 0
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)

	if not isLeft: # Account for left column edge case
		if previousState[row][col - 1] == '#':
			thisCount += 1 # Middle Left

	if not isRight: # Account for right column edge case
		if previousState[row][col + 1] == '#':
			thisCount += 1 # Middle Right

	return(thisCount)
def checkBelow(row, col, previousState):
	thisCount = 0
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)

	if not isLeft: # Account for left column edge case
		if previousState[row + 1][col - 1] == '#':
			thisCount += 1 # Bottom Left

	if previousState[row + 1][col] == '#':
		thisCount += 1 # Bottom Middle

	if not isRight: # Account for right column edge case
		if previousState[row + 1][col + 1] == '#':
			thisCount += 1 # Bottom Right

	return(thisCount)

# Import data
initialSeats = open('input.txt', 'r').read().splitlines()

# Initially occupy all seats

# Prep for iteration
totalRows = len(initialSeats)
totalCols = len(initialSeats[0])
global totalCounts
totalCounts = (totalRows, totalCols)
newState = initialSeats.copy() # For comparison

while True:
	row = 0
	col = 0
	previousState = newState.copy()
	newState = []
	# print('Previous:')
	# pprint(previousState)

	for j in range(totalRows):
		newState.append('')
		for i in range(totalCols):
			nearbyOccupied = 0
			if previousState[row][col] == '.':
				newState[row] += '.'
			else:
				# Check top, sides, and below
				if row != 0:
					nearbyOccupied += checkAbove(row, col, previousState)
				nearbyOccupied += checkSides(row, col, previousState)
				if row != totalCounts[0] - 1:
					nearbyOccupied += checkBelow(row, col, previousState)
				
				# Logic for changing seat occupancy
				if previousState[row][col] == 'L' and nearbyOccupied == 0:
					newState[row] += '#'
				elif previousState[row][col] == '#' and nearbyOccupied >= 4:
					newState[row] += 'L'
				else:
					newState[row] += previousState[row][col]
			col += 1
		col = 0
		row += 1
	
	# print('New: ')
	# pprint(newState)
	# print('----------')
	if previousState == newState:
		break

occupiedCount = 0
for i in newState:
	for j in i:
		if j == '#':
			occupiedCount += 1
print('Occupied Seats: ' + str(occupiedCount))