# Day 08
from pprint import pprint

# List with all of the numbers and their corresponding segment
# The number 8 would be rendered using the following segments

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

allNums = [
    ['a','b','c','e','f','g'],
    ['c','f'],
    ['a','c','d','e','g'],
    ['a','c','d','f','g'],
    ['b','c','d','f'],
    ['a','b','d','f','g'],
    ['a','b','d','e','f','g'],
    ['a','c','f'],
    ['a','b','c','d','e','f','g'],
    ['a','b','c','d','f','g']
]

# Data is prepared as a list of tuples. Each tuple has the following structure:
# Tuple = ([signals], [outputs])
# Signals and outputs are both lists of strings

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
    return data

def part1(data):
    numberCounter = {}
    for i in range(0, 10):
        numberCounter[i] = 0

    for line in data:
        for signal in line[1]:
            if len(signal) == 2:
                numberCounter[1] += 1
            elif len(signal) == 3:
                numberCounter[7] += 1
            elif len(signal) == 4:
                numberCounter[4] += 1
            elif len(signal) == 7:
                numberCounter[8] += 1
    
    sum = numberCounter[1] + numberCounter[7] + numberCounter[4] + numberCounter[8]
    
    print('----------')
    print(numberCounter)
    print('----------')
    print(f'Total occurences of 1, 4, 7, 8: {sum}')

def part2(data):
    pass

filepath = 'Day08/sample1.txt'
# filepath = 'Day08/sample2.txt'
# filepath = 'Day08/input.txt'

data = prepareData(filepath)
part1(data)