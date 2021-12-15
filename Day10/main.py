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

def checkScore2(line, points):
    score = 0
    for char in line[-1::-1]:
        score *= 5
        score += points[char]
    return score

isSample = False
data = prepareData(isSample)
pairs = ['()', '[]', '{}', '<>']
openingTags = ['(', '[', '{', '<']
closingTags = [')', ']', '}', '>']
incompletePoints = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
completePoints = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
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
# Generate a list of corrupted lines
corruptedLines = []
for i in range(len(data)):
    for mismatch in mismatches:
        if mismatch in data[i]:
            corruptedLines.append(data[i])

# Get the score for incomplete 
score = 0
for line in corruptedLines:
    score += checkScore(line, incompletePoints)
print(f'Part 1 Score: {score}')

# Get a list of the incomplete lines
incompleteLines = []
for line in data:
    if line not in corruptedLines:
        incompleteLines.append(line)

# Calculate the scores for each incomplete line
scores = [checkScore2(line, completePoints) for line in incompleteLines]
winningScore = sorted(scores)[len(scores)//2]
print('Part 2 Scores:')
pprint(scores)
print(f'Winning Score: {winningScore}')