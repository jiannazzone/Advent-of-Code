# Advent of Code 2015-2

filename = '/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day02/input1.txt'
with open(filename) as f:
    rawData = f.read().split('\n')

data = []
for line in rawData:
    thisBox = [int(x) for x in line.split('x')]
    data.append(thisBox)

def calculateSurfaceArea(boxDimensions):
    sides = []
    sides.append(2*boxDimensions[0]*boxDimensions[1])
    sides.append(2*boxDimensions[1]*boxDimensions[2])
    sides.append(2*boxDimensions[2]*boxDimensions[0])
    sides.sort()

    totalSurface = 0
    for side in sides:
        totalSurface += side
    totalSurface += (sides[0] / 2)
    return totalSurface

# Part 1
totalArea = 0
for line in data:
    totalArea += int(calculateSurfaceArea(line))
print(f'Total wrapping paper: {totalArea} sq. ft')

# Part 2
