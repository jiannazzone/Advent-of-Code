# Day 15
from pprint import pprint
import time

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder


def prepareData(isSample):
    if isSample:
        filepath = 'Day15/sample.txt'
    else:
        filepath = 'Day15/input.txt'

    with open(filepath) as f:
        data = [[int(x) for x in row] for row in f.read().split('\n')]

    return data


def part1(isSample):
    # Find the path with the lowest sum of values that leads from the
    # top-left to the bottom-right of the array
    # You can only move in the 4 cardinal directions
    # When finding the sum, do not count the starting position

    # Use pathfinding package
    data = prepareData(isSample)
    grid = Grid(matrix=data)

    start = grid.node(0, 0)
    end = grid.node(len(data)-1, len(data[0])-1)

    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    # Get sum of all values along path, subtracting the initial position
    sum = 0
    for coordinate in path:
        sum += data[coordinate[1]][coordinate[0]]
    sum -= data[0][0]
    
    print(f'Path Sum: {sum}')

def part2(isSample):
    startingGrid = prepareData(isSample)
    
    # Prepare 5x5 repeating grid of data
    # Danger levels increase by one each time that you increment the column or row
    # A level 9 wraps around to 1. For example:
    # The left shows how values change each iteration
    # The right shows which grids are identical to each other
    # # # # # # # -- # # # # # # #
    # 8 9 1 2 3 # -- # 0 1 2 3 4 #
    # 9 1 2 3 4 # -- # 1 2 3 4 5 #
    # 1 2 3 4 5 # -- # 2 3 4 5 6 #
    # 2 3 4 5 6 # -- # 3 4 5 6 7 #
    # 3 4 5 6 7 # -- # 4 5 6 7 8 #
    # # # # # # # -- # # # # # # # 

    # Create 9 iterations of the grid. The first iteration is just the original grid
    allIterations = [startingGrid]
    
    # We need 8 more iterations of the grid
    lastIteration = startingGrid
    for i in range(8):
        thisIteration = []
        for row in lastIteration:
            newRow = []
            for num in row:
                if num == 9:
                    newRow.append(1)
                else:
                    newRow.append(num + 1)
            thisIteration.append(newRow)
        allIterations.append(thisIteration)
        lastIteration = thisIteration
    
    # Now that we have all the ierations, it's just a matter of concatenating them appropriately
    finalGrid = []
    
    for i in range(5):
        # Iterate across each 'meta-row' corresponding to one row of concatenated grids
        for row in range(len(allIterations[0])):
            thisRow = []
            for j in range(5):
                rowToAdd = allIterations[i + j][row]
                for num in rowToAdd:
                    thisRow.append(num)
            finalGrid.append(thisRow)
    
    print('Final Grid Assembled; now pathfinding. This could take a while...')
    print(f'Your grid is {len(finalGrid)} x {len(finalGrid[0])}')

    # -- Debugging -- #
    # with open('Day15/sampleGiantGrid.txt') as f:
    #     sampleGrid = [[int(x) for x in row] for row in f.read().split('\n')]
    
    # if sampleGrid == finalGrid:
    #     print('Huzzah!')
    # -- Debugging -- #

    # Now we just need to pathfind! Copy code from Part 1
    grid = Grid(matrix=finalGrid)

    start = grid.node(0, 0)
    end = grid.node(len(finalGrid)-1, len(finalGrid[0])-1)

    finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    # Get sum of all values along path, subtracting the initial position
    sum = 0
    for coordinate in path:
        sum += finalGrid[coordinate[1]][coordinate[0]]
    sum -= finalGrid[0][0]
    
    print(f'Path Sum: {sum}')

start_time = time.time()
isSample = False
print('\n--- Part 1 ---')
part1(isSample)

print('\n--- Part 2 ---')
part2(isSample)