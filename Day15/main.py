# Day 15
from pprint import pprint

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


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

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
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
    # 8 9 1 2 3 # -- # 1 2 3 4 5 #
    # 9 1 2 3 4 # -- # 2 3 4 5 6 #
    # 1 2 3 4 5 # -- # 3 4 5 6 7 #
    # 2 3 4 5 6 # -- # 4 5 6 7 8 #
    # 3 4 5 6 7 # -- # 5 6 7 8 9 #
    # # # # # # # -- # # # # # # #

    # Create 9 iterations of the grid. The first iteration is just the original grid
    allIterations = [startingGrid]

    with open('Day15/sampleGiantGrid.txt') as f:
        sampleGrid = [[int(x) for x in row] for row in f.read().split('\n')]
    
    # if sampleGrid == newGrid:
    #     print('Huzzah!')

isSample = True
# part1(isSample)
part2(isSample)