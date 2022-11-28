# Advent of Code 2015 Day 5

filename = '/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day05/input.txt'
with open(filename) as f:
    data = f.read().split('\n')

vowels = ['a', 'e', 'i', 'o', 'u']

# Part 1 Functions
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

def part1():
    niceLines = []
    for line in data:
        if checkIllegal(line) and checkForDouble(line) and checkVowels(line):
            niceLines.append(line)
    print(f'\n-----Part 1-----\nThis data set has {len(niceLines)} nice lines.\n')

# Part 2 Functions
def checkForXYX(line):
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            return True
    # If we exited the for-loop, then there are no XYX patterns
    return False

def checkForRepeatDoubles(line):
    pairs = []
    for i in range(len(line)-1):
        pairs.append(f'{line[i]}{line[i+1]}')
    for i in range(len(pairs)-1):
        if pairs[i] in pairs[i+2:]:
            return True
    # If we reached this point, there are no pairs 
    return False

def part2():
    niceLines = []
    for line in data:
        if checkForRepeatDoubles(line) and checkForXYX(line):
            niceLines.append(line)
    print(f'\n-----Part 2-----\nThis data set has {len(niceLines)} nice lines.\n')

# Main Code
part1()
part2()