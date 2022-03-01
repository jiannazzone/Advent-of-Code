# Advent of Code 2015 Day 5

filename = '/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day05/input.txt'
with open(filename) as f:
    data = f.read().split('\n')

vowels = ['a', 'e', 'i', 'o', 'u']

def checkVowels(line):
    vowelCount = 0
    for letter in line:
        if letter in vowels:
            vowelCount += 1
    if vowelCount >= 3:
        return True
    else:
        return False

def checkIllegal(line):
    if 'ab' in line:
        return False
    elif 'cd' in line:
        return False
    elif 'pq' in line:
        return False
    elif 'xy' in line:
        return False
    else:
        return True

def checkForDouble(line):
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            return True

    # If we reached this point, there are no double letters
    return False

def part1() :
    niceLines = []
    for line in data:
        if checkIllegal(line) and checkForDouble(line) and checkVowels(line):
            niceLines.append(line)
    print(f'This data set has {len(niceLines)} nice lines.')

part1()