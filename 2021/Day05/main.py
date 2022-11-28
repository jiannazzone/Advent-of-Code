# Day 05

from pprint import pprint

# filepath = 'Day05/sample.txt'
filepath = 'Day05/input.txt'

ventMap = []
ventData = []

def prepareData():

    with open(filepath) as f:
        data = f.read().split('\n')

    '''
    Each entry in ventData is formatted as follows:
    entry = {
        "x1": value,
        "y1": value,
        "x2": value,
        "y2": value
    }
    '''

    for line in data:
        thisLine = line.split(' -> ')
        firstCoordinate = [int(x) for x in thisLine[0].split(',')]
        secondCoordinate = [int(x) for x in thisLine[1].split(',')]
        thisEntry = {
            'x1': firstCoordinate[0],
            'y1': firstCoordinate[1],
            'x2': secondCoordinate[0],
            'y2': secondCoordinate[1]
        }
        ventData.append(thisEntry)

    ventMap = createBlankMap()

    return ventMap, ventData

def createBlankMap():
    # Get the max for x and y to create an empty 2D list
    xMax = 0
    yMax = 0

    for item in ventData:
        # x-values
        if item['x1'] > xMax:
            xMax = item['x1']
        if item['x2'] > xMax:
            xMax = item['x2']
        
        # y-values
        if item['y1'] > yMax:
            yMax = item['y1']
        if item['y2'] > yMax:
            yMax = item['y2']

    # print("Max x-value: " + str(xMax))
    # print("Max y-value: " + str(yMax))

    ventMap = [[0 for x in range(xMax + 1)] for y in range(yMax + 1)]
    return ventMap

def markTheMap(includeDiagonals):

    for entry in ventData:

        # Check for horizontal lines
        if entry['y1'] == entry['y2']:
            row = entry['y1']
            # Determine start and stop column... data could be presented as increasing or decreasing x-values
            if entry['x1'] < entry['x2']:
                startCol = entry['x1']
                stopCol = entry['x2'] + 1
            else:
                startCol = entry['x2']
                stopCol = entry['x1'] + 1
            
            # Increment the count on each grid point in the line
            for col in range(startCol, stopCol):
                ventMap[row][col] += 1
        
        # Check for vertical lines
        elif entry['x1'] == entry['x2']:
            col = entry['x1']
            # Determine start and stop row... data could be presented as increasing or decreasing y-values
            if entry['y1'] < entry['y2']:
                startRow = entry['y1']
                stopRow = entry['y2'] + 1
            else:
                startRow = entry['y2']
                stopRow = entry['y1'] + 1
            
            # Increment the count on each grid point in the line
            for row in range(startRow, stopRow):
                ventMap[row][col] += 1
        
        #Check for diagonal lines
        if includeDiagonals:
            # Ensure that it's a 45-degree diagonal
            xLength = abs(entry['x1'] - entry['x2'])
            yLength = abs(entry['y1'] - entry['y2'])

            # Arrange points so that first point always has the lower x-value
            if xLength == yLength:
                if entry['x1'] < entry['x2']:
                    firstPoint = (entry['x1'], entry['y1'])
                    secondPoint = (entry['x2'], entry['y2'])
                else:
                    firstPoint = (entry['x2'], entry['y2'])
                    secondPoint = (entry['x1'], entry['y1'])
                
                if firstPoint[1] > secondPoint[1]:
                    diagonalUp = True
                else:
                    diagonalUp = False
                
                if diagonalUp:
                    col = firstPoint[0]
                    for row in range(firstPoint[1], secondPoint[1] -1, -1):
                        ventMap[row][col] += 1
                        col += 1
                else:
                    col = firstPoint[0]
                    for row in range(firstPoint[1], secondPoint[1] + 1):
                        ventMap[row][col] += 1
                        col += 1
                


def countTheMap():
    intersectionCount = 0
    for row in ventMap:
        for num in row:
            if num > 1:
                intersectionCount += 1
    print('Total intersections: ' + str(intersectionCount))

ventMap, ventData = prepareData()

print('\nPart 1:\n-----')
markTheMap(False)
countTheMap()

print('\nPart 2:\n-----')
ventMap = createBlankMap()
markTheMap(True)
countTheMap()
# pprint(ventMap)