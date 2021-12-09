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
    

def part1(data):
    totalRiskLevel = 0
    # Iterate through each item
    # Check left, right, up, down
    for row in range(len(data)):
        for col in range(len(data[0])):
            totalRiskLevel += checkNeighbors(row, col, data)

    print(f'Total Risk Level: {totalRiskLevel}')

# filepath = 'Day09/sample.txt'
filepath = 'Day09/input.txt'
data = prepareData()
part1(data)