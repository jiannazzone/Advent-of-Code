# Day 4
from pprint import pprint

def processInput(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    allPairs = []
    for pair in data:
        thisPairRaw = [x.split('-') for x in pair.split(',')]
        thisPair = []
        for elf in thisPairRaw:
            thisPair.append([int(x) for x in elf])
        allPairs.append(thisPair)
    print(data)
    pprint(allPairs)

filename = 'Day04/sample.txt'
processInput(filename)