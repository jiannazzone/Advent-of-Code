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
def checkUp(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isTop:
		for i in range(row):
			thisRow = row - 1 - i
			if previousState[thisRow][col] == '#':
				return 1
				break
			elif previousState[thisRow][col] == 'L':
				return 0
				break
	return 0
def checkDown(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isBottom:
		for i in range(1, len(previousState) - row):
			thisRow = row + i
			if previousState[thisRow][col] =='#':
				return 1
				break
			elif previousState[thisRow][col] =='L':
				return 0
				break
	return 0
def checkLeft(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isLeft:
		for i in range(col):
			thisCol = col - 1 - i
			if previousState[row][thisCol] == '#':
				return 1
				break
			elif previousState[row][thisCol] == 'L':
				return 0
				break
	return 0
def checkRight(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isRight:
		for i in range(1, len(previousState[row]) - col):
			thisCol = col + i
			if previousState[row][thisCol] == '#':
				return 1
				break
			elif previousState[row][thisCol] == 'L':
				return 0
				break
	return 0
def checkUpLeft(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isLeft and not isTop:
		# Get number of moves
		for i in range(totalCounts[0]*totalCounts[1]):
			thisCol = col - 1 - i
			thisRow = row - 1 - i
			if previousState[thisRow][thisCol] == '#':
				return 1
				break
			elif previousState[thisRow][thisCol] == 'L':
				return 0
				break
			if thisRow == 0 or thisCol == 0:
				return 0
				break
	return 0
def checkUpRight(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isRight and not isTop:
		# Get number of moves
		for i in range(totalCounts[0]*totalCounts[1]):
			thisCol = col + 1 + i
			thisRow = row - 1 - i
			if previousState[thisRow][thisCol] == '#':
				return 1
				break
			elif previousState[thisRow][thisCol] == 'L':
				return 0
				break
			if thisRow == 0 or thisCol == totalCounts[1] - 1:
				return 0
				break
	return 0
def checkDownLeft(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isLeft and not isBottom:
		# Get number of moves
		for i in range(totalCounts[0]*totalCounts[1]):
			thisCol = col - 1 - i
			thisRow = row + 1 + i
			if previousState[thisRow][thisCol] == '#':
				return 1
				break
			elif previousState[thisRow][thisCol] == 'L':
				return 0
				break
			if thisRow == totalCounts[0] - 1 or thisCol == 0:
				return 0
				break
	return 0
def checkDownRight(row, col, previousState):
	(isTop, isRight, isBottom, isLeft) = checkRowAndCol(row, col)
	if not isRight and not isBottom:
		for i in range(totalCounts[0]*totalCounts[1]):
			thisCol = col + 1 + i
			thisRow = row + 1 + i
			if previousState[thisRow][thisCol] == '#':
				return 1
				break
			elif previousState[thisRow][thisCol] == 'L':
				return 0
				break
			if thisRow == totalCounts[0] - 1 or thisCol == totalCounts[1] - 1:
				return 0
				break
	return 0

# Import data
initialSeats = open('input.txt', 'r').read().splitlines()

# Initially occupy all seats

# Prep for iteration
totalRows = len(initialSeats)
totalCols = len(initialSeats[0])
global totalCounts
totalCounts = (totalRows, totalCols)
newState = initialSeats.copy()

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
				# Check top, sides, below, and 4 diagonals
				nearbyOccupied += checkUp(row, col, previousState)
				nearbyOccupied += checkDown(row, col, previousState)
				nearbyOccupied += checkLeft(row, col, previousState)
				nearbyOccupied += checkRight(row, col, previousState)
				nearbyOccupied += checkUpLeft(row, col, previousState)
				nearbyOccupied += checkUpRight(row, col, previousState)
				nearbyOccupied += checkDownLeft(row, col, previousState)
				nearbyOccupied += checkDownRight(row, col, previousState)
				
				# Logic for changing seat occupancy
				if previousState[row][col] == 'L' and nearbyOccupied == 0:
					newState[row] += '#'
				elif previousState[row][col] == '#' and nearbyOccupied >= 5:
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