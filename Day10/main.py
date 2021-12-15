# Day 10
from os import close
from pprint import pprint
import re

def prepareData(isSample):
    if isSample:
        filepath = 'Day10/sample.txt'
    else:
        filepath = 'Day10/input.txt'
    with open(filepath) as f:
        data = f.read().split('\n')
    return data

def checkScore(line, points):
    for character in line:
        if character in points:
            return points[character]

def part1(isSample):
    data = prepareData(isSample)
    pairs = ['()', '[]', '{}', '<>']
    openingTags = ['(', '[', '{', '<']
    closingTags = [')', ']', '}', '>']
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    
    mismatches = []
    for i in range(len(openingTags)):
        for j in range(len(closingTags)):
            if i != j:
                mismatches.append(openingTags[i] + closingTags[j])

    # Loop through each line of data and reduce until no more changes are being applied
    while True:
        p = re.compile('|'.join(map(re.escape, pairs)))
        reducedData = [p.sub('', s) for s in data]
        if reducedData == data:
            break
        else:
            data = reducedData
    
    # Once reduced look for mismatched pairs
    # Generate an index os corrupted lines
    corruptedLines = []
    for i in range(len(data)):
        for mismatch in mismatches:
            if mismatch in data[i]:
                corruptedLines.append(data[i])
    
    pprint(corruptedLines)
    
    # Get the score
    score = 0
    for line in corruptedLines:
        score += checkScore(line, points)
    print(f'Final score: {score}')

isSample = False
part1(isSample)