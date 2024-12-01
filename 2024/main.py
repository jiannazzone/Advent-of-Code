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
totalDifference = 0

for i in range(len(list1)):
    totalDifference += abs(list1[i] - list2[i])

print(f'Difference score: {totalDifference}')


# Part 2
similarityScore = 0
list2Count = collections.Counter(list2)
for x in list1:
    if x in list2Count.keys():
        similarityScore += x * list2Count[x]

print(f'Similarity Score: {similarityScore}')