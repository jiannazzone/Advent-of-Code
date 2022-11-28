# Day 09
from pprint import pprint

def prepareData():
    with open(filepath) as f:
        rawData = f.read().split('\n')
    
    data = []
    for line in rawData:
        thisLine = [int(x) for x in line]
        data.append(thisLine)
    return data

def checkNeighbors(row, col, data):
    thisVal = data[row][col]

    # Check left if not first column
    if col > 0:
        if thisVal < data[row][col-1]:
            pass
        else:
            return 0
    
    # Check right if not last column
    if col < len(data[0]) - 1:
        if thisVal < data[row][col+1]:
            pass
        else:
            return 0
    
    # Check up if not top row
    if row > 0:
        if thisVal < data[row-1][col]:
            pass
        else:
            return 0
    
    # Check down if not bottom row
    if row < len(data) - 1:
        if thisVal < data[row+1][col]:
            pass
        else:
            return 0
    # If pass through all checks, return danger level
    return thisVal + 1

def getLowPoints(row, col, data):
    thisVal = data[row][col]

    # Check left if not first column
    if col > 0:
        if thisVal < data[row][col-1]:
            pass
        else:
            return (-1, -1)
    
    # Check right if not last column
    if col < len(data[0]) - 1:
        if thisVal < data[row][col+1]:
            pass
        else:
            return (-1, -1)
    
    # Check up if not top row
    if row > 0:
        if thisVal < data[row-1][col]:
            pass
        else:
            return (-1, -1)
    
    # Check down if not bottom row
    if row < len(data) - 1:
        if thisVal < data[row+1][col]:
            pass
        else:
            return (-1, -1)
    # If pass through all checks, return danger level
    return (row, col)

def checkNeighbors2(row, col, data, visitedMap):
    thisVal = data[row][col]
    thisBasinCount = 0

    # Only check values with a zero
    if thisVal == 0:
        thisBasinCount += 1
        visitedMap[row][col] = True
        # Check left if not first column
        if col > 0:
            if data[row][col-1] == 0:
                thisBasinCount += 1
            visitedMap[row][col-1] = True
        
        # Check right if not last column
        if col < len(data[0]) - 1:
            if data[row][col+1] == 0:
                thisBasinCount += 1
            visitedMap[row][col+1] = True
        
        # Check up if not top row
        if row > 0:
            if data[row-1][col] == 0:
                thisBasinCount += 1
            visitedMap[row-1][col] = True
        
        # Check down if not bottom row
        if row < len(data) - 1:
            if data[row+1][col] == 0:
                thisBasinCount += 1
            visitedMap[row+1][col] = True
    
    # pprint(visitedMap)
    return thisBasinCount

def findBasinSize(coordinate, data, visitedMap):
    # Add one to the row/col coordinate to account for the border of 9s that I added
    newCoordinate = (coordinate[0] + 1, coordinate[1] + 1)
    basinSize = 0

    # Starting from the coordinate (row, col), spiral outward until the basin size is fixed?
    

    return visitedMap, basinSize


def part1(data):
    totalRiskLevel = 0
    # Iterate through each item
    # Check left, right, up, down
    for row in range(len(data)):
        for col in range(len(data[0])):
            totalRiskLevel += checkNeighbors(row, col, data)

    print(f'Total Risk Level: {totalRiskLevel}')

def part2(data):

    # Find all of the low points in the data set
    lowPoints = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            coordinate = getLowPoints(row, col, data)
            if coordinate[0] != -1:
                lowPoints.append(coordinate)
    
    # Add a border of 9s all around the dataset. Idk maybe this will help?
    newDataSet = []
    newDataSet.append([9 for x in range(len(data[0]) + 2)])
    for line in data:
        newLine = [9]
        for char in line:
            newLine.append(char)
        newLine.append(9)
        newDataSet.append(newLine)
    newDataSet.append([9 for x in range(len(data[0]) + 2)])

    # Starting from those low points, spiral out and find the size of each basin
    # Once the basin is enclosed, add its size to the list
    visitedMap = [[False for col in range(len(newDataSet[0]))] for row in range(len(newDataSet))]
    basinSizes = []
    for coordinate in lowPoints:
        thisBasinSize, visitedMap = findBasinSize(coordinate, newDataSet, visitedMap)


filepath = 'Day09/sample.txt'
# filepath = 'Day09/input.txt'
data = prepareData()
# part1(data)
part2(data)