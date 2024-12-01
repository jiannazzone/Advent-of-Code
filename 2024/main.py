# Day 01

from pprint import pprint
import collections

samplePath = 'sample_a.txt'
inputPath = 'input_a.txt'

def parseInput(filepath):
    with open(filepath, 'r') as f:
        data = f.read().splitlines()

    list1 = []
    list2 = []
    for line in data:
        thisLine = line.split('   ')
        list1.append(int(thisLine[0]))
        list2.append(int(thisLine[1]))
    return list1, list2

list1, list2 = parseInput(inputPath)

# Part 1
list1.sort()
list2.sort()
differenceScore = 0

# Get difference between each element in ordered lists, then add that difference to the total
for i in range(len(list1)):
    differenceScore += abs(list1[i] - list2[i])

print(f'Difference score: {differenceScore}')


# Part 2
similarityScore = 0

# Get a frequency count for each element in list2
list2Count = collections.Counter(list2)

# Multiply each element in list1 by its frequency in list2
# Skip elements that do not appear in list2
for x in list1:
    if x in list2Count.keys():
        similarityScore += x * list2Count[x]

print(f'Similarity Score: {similarityScore}')