# Day 08
from pprint import pprint

def prepareData(filepath):
    with open(filepath) as f:
        rawData = f.read().split('\n')

    data = []
    for line in rawData:
        formattedLine = line.split(' | ')
        patterns = formattedLine[0].split(' ')
        output = formattedLine[1].split(' ')
        thisTuple = (patterns, output)
        data.append(thisTuple)

filepath = 'Day08/sample.txt'
# filepath = 'Day08/input.txt'
data = prepareData(filepath)