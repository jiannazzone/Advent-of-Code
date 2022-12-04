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
    # print('All Pairs:')
    # pprint(allPairs)
    return allPairs

filename = 'Day04/input.txt'
allPairs = processInput(filename)

def part1(allPairs):
    # Create an extended list, showing all values for each elf
    allPairsExtended = []
    for pair in allPairs:
        thisPair = []
        for elf in pair:
            thisPair.append(tuple(range(elf[0], elf[1]+1)))
        allPairsExtended.append(thisPair)
    # print('\nAll Pairs Extended')
    # pprint(allPairsExtended)

    overlapCount = 0
    for pair in allPairsExtended:
        if checkForCompleteOverlap(pair):
            overlapCount += 1
    print(f'There are {overlapCount} total overlaps.')

def checkForCompleteOverlap(pair):
    if all(x in pair[0] for x in pair[1]):
        return True
    elif all(x in pair[1] for x in pair[0]):
        return True
    else:
        return False

part1(allPairs)