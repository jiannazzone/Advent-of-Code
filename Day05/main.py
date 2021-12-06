# Day 05

from pprint import pprint

def prepareData():
    filepath = 'Day05/sample.txt'
    # filepath = 'Day05/input.txt'

    with open(filepath) as f:
        data = f.read().split('\n')
    pprint(data)

    '''
    Each entry in ventData is formatted as follows:
    entry = {
        "x1": value,
        "y1": value,
        "x2": value,
        "y2": value
    }
    '''
    ventData = []
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
    pprint(ventData)

prepareData()