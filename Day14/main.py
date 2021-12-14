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

    # Create dictionary with all insertion rules
    # AB -> C becomes the key/val pair 'AB': 'C'
    insertionDictionary = {}
    for rule in data.split('\n')[2:]:
        thisRule = rule.split(' -> ')
        insertionDictionary[thisRule[0]] = thisRule[1]

    return polymerTemplate, insertionDictionary

# --- MAIN CODE --- #
isSample = True
numSteps = 10

polymerString, insertionDictionary = prepareData(isSample)
# print(f'Template: {polymerString}')

# Each part will be examined against the insertion rules
# If a pair matches a rule, a tuple will be generated with the format (position, letter)
# For example: NNCB with an insertion rule of NN -> C will generate a tuple (1, 'C')

# Iterate for a specified number of steps
for step in range(numSteps):
    newPolymerString = ''

    # Look through the entire polymer string
    for i in range(len(polymerString) - 1):
        thisLookup = polymerString[i:i+2]

        # Generate insertion if the pair exists in the insertion dictionary
        if thisLookup in insertionDictionary:
            newString = f'{polymerString[i]}{insertionDictionary[thisLookup]}'
            newPolymerString += newString
    
    newPolymerString += polymerString[-1]
    polymerString = newPolymerString

    # print(f'After step {step+1}: {polymerString}')

# Create dictionary to store letter frequencies
letterFrequency = {}
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letterFrequency[letter] = 0

# Calculate letter frequencies
for letter in polymerString:
    letterFrequency[letter] += 1

# Find min and max letter frequencies
letterFrequencyList = sorted(letterFrequency.values(), reverse=True)
maxLetterFrequency = letterFrequencyList[0]
minLetterFrequency = letterFrequencyList[letterFrequencyList.index(0) - 1]
print(f'Max Letter Frequency: {maxLetterFrequency}')
print(f'Min Letter Frequency: {minLetterFrequency}')

print(f'Frequency Spread: {maxLetterFrequency - minLetterFrequency}')