# Day 8

def processInput(filename):
    with open(filename) as f:
        data = f.read()
    treeMap = [[int(x) for x in line] for line in data.splitlines()]
    return treeMap

treeMap = processInput('Day08/input.txt')

# Part 1
def findVisible():
    # All trees on the edge are visible
    # But we need to be careful not to double-count the corners
    edgeCount = 2*len(treeMap) + 2*(len(treeMap[0])-2)
    visibleTrees = edgeCount

    # Find the max values in each row and each column
    for row in range(1,len(treeMap)-1):
        for col in range(1,len(treeMap[0])-1):
            thisTree = treeMap[row][col]
            visibleTrees += checkTree(thisTree, row, col)
    print(f'There are {visibleTrees} visible trees.')

def checkTree(thisTree, row, col):
    # Check the row
    thisRowCheck = [x < thisTree for x in treeMap[row]]
    if all(thisRowCheck[:col]) or all(thisRowCheck[col+1:]):
        return 1
    
    # Check the column
    thisCol = [x[col] for x in treeMap]
    thisColCheck = [x < thisTree for x in thisCol]
    if all(thisColCheck[:row]) or all(thisColCheck[row+1:]):
        return 1
    
    # Tree not visible
    return 0

findVisible()

# Part 2
def findScenic():
    maxScore = 0
    # We can skip the edge trees, since they will always have a scenic score of 0

    for row in range(1,len(treeMap)-1):
        for col in range(1,len(treeMap[0])-1):
            thisTree = treeMap[row][col]
            thisScore = checkScore(thisTree, row, col)
            if thisScore > maxScore:
                maxScore = thisScore
    print(f'The max possible score is {maxScore}.')

def checkScore(thisTree, row, col):
    left = treeMap[row][:col]
    right = treeMap[row][col+1:]
    up = [x[col] for x in treeMap[:row]]
    down = [x[col] for x in treeMap[row+1:]]
    
    viewCounts = {
        'up': 0,
        'down': 0,
        'left': 0,
        'right': 0
    }

    # Check Up
    for tree in reversed(up):
        if tree < thisTree:
            viewCounts['up'] += 1
        else:
            viewCounts['up'] += 1
            break
    
    # Check Down
    for tree in down:
        if tree < thisTree:
            viewCounts['down'] += 1
        else:
            viewCounts['down'] += 1
            break
    
    # Check Left
    for tree in reversed(left):
        if tree < thisTree:
            viewCounts['left'] += 1
        else:
            viewCounts['left'] += 1
            break
    
    # Check Right
    for tree in right:
        if tree < thisTree:
            viewCounts['right'] += 1
        else:
            viewCounts['right'] += 1
            break
    
    # print(viewCounts)
    score = 1
    for val in viewCounts.values():
        score *= val
    return score

findScenic()