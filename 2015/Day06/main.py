# Advent of Code 2015 Day 6
from pprint import pprint

# Initialize the 1000x1000 grid of all False
from curses import raw
from fileinput import filename


# Part 1
grid = [[False for x in range(1000)] for x in range(1000)]
def processInput():
    filename = '/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day06/input.txt'
    with open(filename) as f:
        rawData = f.read().splitlines()
    
    # Lines are in the format 'command x1,y1 through x2,y2'
    # We need to convert each coordinate into a tuple (x, y) and save each line as ('command', (x, y))
    cleanData = []
    for line in rawData:
        lineList = line.split(' through ')
        
        # Second Coordinate
        b = lineList[-1].split(',')
        b = (int(b[0]), int(b[1]))

        lineList = lineList[0].split(' ')
        # Command and First Coordinate
        if (lineList[0] == 'toggle'):
            command = 'toggle'
        else:
            command = lineList[1]
        
        a = lineList[-1].split(',')
        a = (int(a[0]), int(a[1]))
        cleanData.append((command, a, b))
    return cleanData

def processStep(step):
    # step is in the format (command, a, b)
    # a and b are tuples in the format (row, col)
    command = step[0]
    a = step[1]
    b = step[2]
    for row in range(a[0], b[0] + 1):
        for col in range(a[1], b[1] + 1):
            if command == 'toggle':
                grid[row][col] = not grid[row][col]
            elif command == 'off':
                grid[row][col] = False
            else:
                grid[row][col] = True

def countLights():
    activeLights = 0
    for row in grid:
        for light in row:
            if light:
                activeLights += 1
    print(f'There are {activeLights} currently on.')

def part1():
    instructions = processInput()
    for step in instructions:
        processStep(step)
    countLights()

# Part 2

grid2 = [[0 for x in range(1000)] for x in range(1000)]
def processStep2(step):
    # step is in the format (command, a, b)
    # a and b are tuples in the format (row, col)
    command = step[0]
    a = step[1]
    b = step[2]
    for row in range(a[0], b[0] + 1):
        for col in range(a[1], b[1] + 1):
            if command == 'toggle':
                grid2[row][col] += 2
            elif command == 'off':
                grid2[row][col] -= 1
                if grid2[row][col] < 0:
                    grid2[row][col] = 0
            else:
                grid2[row][col] += 1

def sumBrightnesses():
    totalBrightness = 0
    for row in grid2:
        for light in row:
            totalBrightness += light
    print(f'The total brightness is {totalBrightness}.')
def part2():
    instructions = processInput()
    for step in instructions:
        processStep2(step)
    sumBrightnesses()

part1()
part2()