#  Day 3
import string
from pprint import pprint

def processInput(filename):
    with open(filename) as f:
        data = f.read().split('\n')
    return data
    
filename = 'Day03/input.txt'
data = processInput(filename)
priorityList = list(string.ascii_letters)


# Part 1
def part1(data):
    rucksacks = [ (x[:len(x)//2], x[len(x)//2:]) for x in data]
    # Determine which letters are in common for each compartment of each rucksack
    lettersInCommon = []
    for r in rucksacks:
        lettersInCommon.append(findLetterInCommon(r))
    # print(lettersInCommon)
    print(f'Part 1 Priority Sum: {getPrioritySum(lettersInCommon)}')
   

def findLetterInCommon(rucksack):
    for letter in rucksack[0]:
        if letter in rucksack[1]:
            return letter

def getPrioritySum(lettersInCommon):
     # Get priority of each letter and sum
    prioritySum = 0
    for letter in lettersInCommon:
        prioritySum += priorityList.index(letter) + 1
    return prioritySum

part1(data)

# Part 2
def part2(rucksacks):

    # Split rucksacks into triplet groups
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i+3])
    
    # For each group, find the common letter
    lettersInCommon = []
    for group in groups:
        lettersInCommon.append(findGroupLetter(group))
    # print(lettersInCommon)

    print(f'Part 2 Priority Sum: {getPrioritySum(lettersInCommon)}')


def findGroupLetter(group):
    # For each letter in first bag, see what is in common with bag 2
    # If that letter is in bag 2, check bag 3
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            return letter

part2(data)