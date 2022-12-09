# Day 8

def processInput(filename):
    with open(filename) as f:
        data = f.read()
    treeMap = [[int(x) for x in line] for line in data.splitlines()]
    return treeMap

treeMap = processInput('Day08/sample.txt')

def findVisible():
    # All trees on the edge are visible
    # But we need to be careful not to double-count the corners
    edgeCount = 2*len(treeMap) + 2*(len(treeMap[0])-2)
    visibleTrees = edgeCount

    # Find the max values in each row and each column
    rowMax = []
    for row in treeMap:
        rowMax.append(max(row))
    
    colMax = []
    for i in range(len(treeMap[0])):
        thisCol = [x[i] for x in treeMap]
        colMax.append(max(thisCol))

    for row in range(1,len(treeMap)-1):
        for col in range(1,len(treeMap[0])-1):
            thisTree = treeMap[row][col]
            visibleTrees += checkTree(thisTree, row, col)
    print(visibleTrees)

def checkTree(thisTree, row, col):
    # Check the row
    thisRowCheck = [x < thisTree for x in treeMap[row]]
    if all(thisRowCheck[:col-1]) or all(thisRowCheck[col+1:]):
        return 1
    
    # Check the column
    thisCol = [x[col] for x in treeMap]
    thisColCheck = [x < thisTree for x in thisCol]
    if all(thisColCheck[:row-1]) or all(thisColCheck[row+1:]):
        return 1
    
    # Tree not visible
    return 0

findVisible()