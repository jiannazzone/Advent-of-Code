# Day 08
from pprint import pprint

# Dictionary with all of the numbers and their corresponding segments
# The number 8 would be rendered using the following segments

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

allNums = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

# Data is prepared as a list of tuples. Each tuple has the following structure:
# Tuple = ([signals], [outputs])
# Signals and outputs are both lists of strings

def prepareData(filepath):
    with open(filepath) as f:
        rawData = f.read().split('\n')

    data = []
    for line in rawData:
        formattedLine = line.split(' | ')
        patterns = formattedLine[0].split(' ')
        output = formattedLine[1].split(' ')
        thisTuple = (patterns, output)
        data.append(thisTuple)
    return data

def part1(data):
    numberCounter = {}
    for i in range(0, 10):
        numberCounter[i] = 0

    for line in data:
        for signal in line[1]:
            if len(signal) == 2:
                numberCounter[1] += 1
            elif len(signal) == 3:
                numberCounter[7] += 1
            elif len(signal) == 4:
                numberCounter[4] += 1
            elif len(signal) == 7:
                numberCounter[8] += 1
    
    sum = numberCounter[1] + numberCounter[7] + numberCounter[4] + numberCounter[8]
    
    print('----------')
    print(numberCounter)
    print('----------')
    print(f'Total occurences of 1, 4, 7, 8: {sum}')

def part2(data):

    for entry in data:
        # Prepare an empty dictionary to store the number mappings for this entry
        thisMapping = {}
        for i in range(0, 10):
            thisMapping[i] = ''

        # Solve the easy digits first
        for signal in entry[0]:
            signalLength = len(signal)
            if signalLength == 2:
                thisMapping[1] = signal
            elif signalLength == 3:
                thisMapping[7] = signal
            elif signalLength == 4:
                thisMapping[4] = signal
            elif signalLength == 7:
                thisMapping[8] = signal
        
        # The keys for this dictionary correspond to "standard" 7-segment display locations (see top of file)
        # The value correspond to what "letter" lights that location in THIS entry
        thisSegmentMapping = {
            'a': '',
            'b': '',
            'c': '',
            'd': '',
            'e': '',
            'f': '',
            'g': ''
        }

        # Now that we know 1 and 7, we can deduce which letter lights up the "a" location
        for letter in thisMapping[7]:
            if letter not in thisMapping[1]:
                thisSegmentMapping['a'] = letter
                break
        
        # Make lists of the signals with 5 letters and 6 letters for comparisons
        fiveLetterNumbers = []
        sixLetterNumbers = []
        for signal in entry[0]:
            if len(signal) == 5:
                fiveLetterNumbers.append(signal)
            elif len(signal) == 6:
                sixLetterNumbers.append(signal)

        # Compare all of the 5-letter signals
        # For the three signals, they all share three letters. Those are the a, d and g letters
        # Then see which of those is present in 4... that is your d. The other is g
        
        commonLetters = ''
        for letter in fiveLetterNumbers[0]:
            if letter in fiveLetterNumbers[1] and letter in fiveLetterNumbers[2]:
                commonLetters += letter

        for letter in commonLetters:
            if letter != thisSegmentMapping['a']:
                if letter in thisMapping[4]:
                    thisSegmentMapping['d'] = letter
                else:
                    thisSegmentMapping['g'] = letter
        
        # Now that we know all the horizontal letters, we can deduce the signal for 0
        # Of the 6-letter signals, 0 is missing one of the horizonal letters
        horizontalLetters = [thisSegmentMapping['a'],thisSegmentMapping['d'], thisSegmentMapping['g']]
        for signal in sixLetterNumbers:
            if not all((x in signal) for x in horizontalLetters):
                thisMapping[0] = signal

        # Function output
        print('Letter mappings: ')
        print(thisSegmentMapping)
        print('----------')
        print(f'Solved numbers:')
        print(thisMapping)


filepath = 'Day08/sample1.txt'
# filepath = 'Day08/sample2.txt'
# filepath = 'Day08/input.txt'

data = prepareData(filepath)
# part1(data)
part2(data)