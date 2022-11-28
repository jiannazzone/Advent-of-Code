# Advent of Code 2015 Day 7
from curses import raw
from fileinput import filename
from pprint import pprint

def prepareData(filename):
    filepath = f'/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day07/{filename}.txt'
    with open(filepath) as f:
        rawData = f.read().splitlines()
    
    allInstructions = []
    for line in rawData:
        # Instructions are stored as [input, output]
        allInstructions.append(line.split(' -> '))
    pprint(allInstructions)
    allWires = {}
    for line in allInstructions:
        allWires[line[1]] = 0
    pprint(allWires)

prepareData('sample')