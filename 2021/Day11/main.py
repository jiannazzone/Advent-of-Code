# Day 11
from pprint import pprint

def prepareData(isSample):
    if isSample:
            filepath = 'Day11/sample.txt'
    else:
        filepath = 'Day11/input.txt'

    with open(filepath) as f:
        rawData = f.read().split('\n')
    
    data = [[int(x) for x in row] for row in rawData]

    return data

def flashThisOctopus(data, row, col):
    # Check octopi in all 8 adjacent spaces
    # and increment them by one

    # Check row above
    if row > 0:
        # Top Left
        if col > 0:
            data[row-1][col-1] += 1
        # Top Middle
        data[row-1][col] += 1
        # Top Right
        if col < len(data[0]) - 1:
            data[row-1][col+1] += 1
    
    # Check same row
    # Left
    if col > 0:
        data[row][col-1] += 1
    # Right
    if col < len(data[0]) - 1:
        data[row][col+1] += 1

    # Check row below
    if row < len(data) - 1:
        # Bottom Left
        if col > 0:
            data[row+1][col-1] += 1
        # Bottom Middle
        data[row+1][col] += 1
        # Bottom Right
        if col < len(data[0]) - 1:
            data[row+1][col+1] += 1

    return data

def flashLoop(flashMap, data, flashCount):
    for row in range(len(data)):
        for col in range(len(data[0])):
            # Flash this octopus if its energy level is greater than 9
            # and hasn't already flashed
            if not flashMap[row][col] and data[row][col] > 9:
                flashMap[row][col] = True
                flashCount += 1
                data = flashThisOctopus(data, row, col)
                return data, flashMap, flashCount

def applySteps(numSteps, data):
    flashCount = 0

    for i in range(numSteps):

        # Create new map for tracking which octopi have flashed
        # Each octopus can only flash once per step
        flashMap = [[False for x in row] for row in data]

        # Increment all octopi by 1
        data = [[x+1 for x in row] for row in data]
        
        # Flash any octopus with a value greater than 9
        # This will loop until there are no more changes for this step
        data, flashMap, flashCount = flashLoop(flashMap, data, flashCount)
        previousFlashMap = flashMap.copy()

        while previousFlashMap is not flashMap:
            data, flashMap, flashCount = flashLoop(flashMap, data, flashCount)
            previousFlashMap = flashMap.copy()
        
        # Check flashMap. Any octopi that flashed get reset to zero
        for row in range(len(flashMap)):
            for col in range(len(flashMap[0])):
                if flashMap[row][col]:
                    data[row][col] = 0
        
        print(f'\nStep {i+1}: ')
        pprint(data)

def part1(isSample, numSteps):
    data = prepareData(isSample)

    print(f'Before any steps:')
    pprint(data)

    applySteps(numSteps, data)

isSample = True
numSteps = 2   
part1(isSample, numSteps)