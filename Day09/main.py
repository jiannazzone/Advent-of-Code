# Day 09
from pprint import pprint
import numpy as np
from scipy import ndimage

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

def part1(data):
    totalRiskLevel = 0
    # Iterate through each item
    # Check left, right, up, down
    for row in range(len(data)):
        for col in range(len(data[0])):
            totalRiskLevel += checkNeighbors(row, col, data)

    print(f'Total Risk Level: {totalRiskLevel}')

def part2(data):

    flattenedMap = []
    visitedMap = [[False for col in range(len(data[0]))] for row in range(len(data))]
    basinSizes = []

    # Make a copy of data with 9 -> 0 and everything else to 1
    # We don't care what values are in the basin
    for row in data:
        thisRow = []
        for num in row:
            if num == 9:
                thisRow.append(1)
            else:
                thisRow.append(0)
        flattenedMap.append(thisRow)
    
    for row in range(len(data)):
        for col in range(len(data[0])):
            if not visitedMap[row][col]:
                thisBasinCount = checkNeighbors2(row, col, flattenedMap, visitedMap)
                if thisBasinCount > 0:
                    basinSizes.append(thisBasinCount)
    print(basinSizes)

    # pprint(flattenedMap)
    # pprint(visitedMap)


filepath = 'Day09/sample.txt'
# filepath = 'Day09/input.txt'
data = prepareData()
# part1(data)
part2(data)