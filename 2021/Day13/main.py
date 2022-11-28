# Day 13
from pprint import pprint

def prepareData(isSample):
    if isSample:
        filepath = 'Day13/sample.txt'
    else:
        filepath = 'Day13/input.txt'

    with open(filepath) as f:
        data = f.read().split('\n')
    
    # Find the empty string and split the data there
    splitIndex = data.index('')
    rawDots = data[:splitIndex]
    rawFolds = data[splitIndex+1:]

    # Convert dots into list of x/y tuples
    dots = []
    for line in rawDots:
        newLine = [int(x) for x in line.split(',')]
        dots.append((newLine[0], newLine[1]))
    
    # Convert foles in list of tuples with the structure (h, 5) or (v, 7)
    folds = []
    for line in rawFolds:
        gLocation = line.index('g')
        newLine = line[gLocation+2:]
        newLine = newLine.split('=')

        if newLine[0] == 'y':
            folds.append(('horizontal',int(newLine[1])))
        else:
            folds.append(('vertical', int(newLine[1])))
    return dots, folds

def makeMap(dots):
    # Find the max row and column in the data sample then generate an empty grid
    # . represent no dot, # represents dot
    # x -> column, y -> row

    maxRow = 0
    maxCol = 0
    for coordinate in dots:
        if coordinate[0] > maxCol:
            maxCol = coordinate[0]
        if coordinate[1] > maxRow:
            maxRow = coordinate[1]
    
    dotGrid = [['.' for x in range(maxCol + 1)] for y in range(maxRow + 1)]
    
    # Iterate through dots and populate dotGrid with 'x' for every coordinate
    for coordinate in dots:
        dotGrid[coordinate[1]][coordinate[0]] = '#'
    
    return dotGrid

def applyFolds(numFolds, dotGrid, folds):

    # Fold the paper and update the dots
    for i in range(numFolds):
        thisFold = folds[i]
        
        if thisFold[0] == 'horizontal':
            # Copy top half of the dot grid (above the fold)
            newDotGrid = dotGrid[:thisFold[1]]

            # Copy bottom half of the dot grid and vertically mirror it
            foldedGrid = dotGrid[:thisFold[1]:-1]

            # Overlay the mirrored grid
            # First row to analyze is  << thisFold[1] - len(foldedGrid) >>
            for row in range(thisFold[1] - len(foldedGrid), len(foldedGrid)):
                for col in range(len(foldedGrid[0])):
                    if foldedGrid[row][col] == '#':
                        newDotGrid[row][col] = '#'
            dotGrid = newDotGrid
        else:
            # Copy the left half of the dot-grid (left of the fold)
            newDotGrid = []
            for row in dotGrid:
                newDotGrid.append(row[:thisFold[1]])
            
            # Copy the right half of the dot-grid and horizontally mirror it
            foldedGrid = []
            for row in dotGrid:
                mirroredRow = row[:thisFold[1]:-1]
                foldedGrid.append(mirroredRow)
            
            # Overlay the mirrored grid
            # First column to analyze is << thisFold[1] - len(foldedGrid[0]) >>
            for row in range(len(newDotGrid)):
                for col in range(thisFold[1] - len(foldedGrid[0]), len(newDotGrid[0])):
                    if foldedGrid[row][col] == '#':
                        newDotGrid[row][col] = '#'
            dotGrid = newDotGrid
        
    # Count the number of '#' character
    # dotCount = 0
    # for row in dotGrid:
    #     for value in row:
    #         if value == '#':
    #             dotCount += 1

    # Print out final answer
    for row in dotGrid:
        print(''.join(row))

def part1():
    dots, folds = prepareData(isSample)
    dotGrid = makeMap(dots)
    applyFolds(1, dotGrid, folds)

def part2():
    dots, folds = prepareData(isSample)
    dotGrid = makeMap(dots)
    applyFolds(len(folds), dotGrid, folds)

isSample = False
# part1()
part2()