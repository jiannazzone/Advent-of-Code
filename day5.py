from pprint import pprint

def splitPass(boardingPass):
	row = boardingPass[:7]
	col = boardingPass[7:]
	return(row, col)
def determineRow(passRow):
	rowRange = [0, 127]
	delta = 64

	for i in range(7):
		if passRow[i] == "F":
			rowRange[1] -= delta
		else:
			rowRange[0] += delta
		delta = delta/2
	return int(rowRange[0])
def determineCol(passCol):
	colRange = [0, 7]
	delta = 4

	for i in range(3):
		if passCol[i] == "L":
			colRange[1] -= delta
		else:
			colRange[0] += delta
		delta = delta/2
	return(int(colRange[0]))
def getSeatID(thisRow, thisCol):
	seatID = thisRow*8 + thisCol
	return(int(seatID))

allPasses = open('input.txt', 'r').read().splitlines()
allSeatIDs = []

for i in allPasses:
	(passRow, passCol) = splitPass(i)
	thisRow = determineRow(passRow)
	thisCol = determineCol(passCol)
	seatID = getSeatID(thisRow, thisCol)
	allSeatIDs.append(seatID)

allSeatIDs.sort(reverse = True)
# print("The highest Seat ID is " + str(allSeatIDs[0]))
# pprint(allSeatIDs)

# START OF PART 2
for i in range(allSeatIDs[-1], allSeatIDs[0] + 1):
	if i not in allSeatIDs:
		print(i)
		break
