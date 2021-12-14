# Day 14
from pprint import pprint

def prepareData(isSample):
    if isSample:
        filepath = 'Day14/sample.txt'
    else:
        filepath = 'Day14/input.txt'

    with open(filepath) as f:
        data = f.read()

    polymerTemplate = data.split('\n\n')[0]
    insertionRules = data.split('\n')[2:]

    # Reformat insertion rules as tuples, where
    # AB -> C become ('AB', 'C')
    for i in range(len(insertionRules)):
        thisRule = insertionRules[i].split(' -> ')
        insertionRules[i] = (thisRule[0], thisRule[1])

    return polymerTemplate, insertionRules

def part1(isSample):
    polymerTemplate, insertionRules = prepareData(isSample)


# --- MAIN CODE --- #
isSample = True
part1(isSample)