#  Day 3
import string

def processInput(filename):
    with open(filename) as f:
        data = f.read().split('\n')
    rucksacks = [ (x[:len(x)//2], x[len(x)//2:]) for x in data]
    return rucksacks
    
filename = 'Day03/input.txt'
rucksacks = processInput(filename)
priorityList = list(string.ascii_letters)


# Part 1
def part1(rucksacks):
    # Determine which letters are in common for each compartment of each rucksack
    lettersInCommon = []
    for r in rucksacks:
        lettersInCommon.append(findLetterInCommon(r))
    # print(lettersInCommon)

    # Get priority of each letter and sum
    prioritySum = 0
    for letter in lettersInCommon:
        prioritySum += priorityList.index(letter) + 1
    print(f'The priority sum is {prioritySum}')

def findLetterInCommon(rucksack):
    for letter in rucksack[0]:
        if letter in rucksack[1]:
            return letter    

part1(rucksacks)