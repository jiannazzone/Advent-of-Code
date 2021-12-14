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

def part1(isSample, numSteps):
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

    pprint(letterFrequency)
    print(f'Max Letter Frequency: {maxLetterFrequency}')
    print(f'Min Letter Frequency: {minLetterFrequency}')
    print(f'Frequency Spread: {maxLetterFrequency - minLetterFrequency}')

def part2(isSample, numSteps):
    polymerString, insertionDictionary = prepareData(isSample)

    # Create first dictionary of letter pairs
    pairFrequencies = {}
    for i in range(len(polymerString) - 1):
        thisPair = polymerString[i:i+2]
        if thisPair in pairFrequencies:
            pairFrequencies[thisPair] += 1
        else:
            pairFrequencies[thisPair] = 1
    
    # Repeat insertion for numSteps
    # We don't care about positioning, and we won't know the actual string at the end
    for step in range(numSteps):
        # For tracking count of each pair
        newPairFrequencies = pairFrequencies.copy()

        # Each key represents at least one occurence of a pair
        # Check that pair for an insertion rule
        for key in pairFrequencies.keys():

            # If insertion rule exists, generate the two new resulting pairs
            if key in insertionDictionary:
                leftPair = key[0] + insertionDictionary[key]
                rightPair = insertionDictionary[key] + key[1]

                # Check each pair to see if it's already in newPairFrequencies
                # If the pair already exists, add to the frequencies
                # Otherwise generate a new key: val entry
                if leftPair in newPairFrequencies:
                    newPairFrequencies[leftPair] += pairFrequencies[key]
                else:
                    newPairFrequencies[leftPair] = pairFrequencies[key]
                
                if rightPair in newPairFrequencies:
                    newPairFrequencies[rightPair] += pairFrequencies[key]
                else:
                    newPairFrequencies[rightPair] = pairFrequencies[key]
                
                newPairFrequencies[key] -= pairFrequencies[key]
        
        # Update our pairFrequencies dictionary in preparation for the next loop
        pairFrequencies = newPairFrequencies

    # Look through pairFrequencies to calculate the occurence of each letter
    letterFrequency = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        letterFrequency[letter] = 0
    
    for key, val in pairFrequencies.items():
        letterFrequency[key[0]] += val
        letterFrequency[key[1]] += val
    
    # Add the first and last letter manually
    letterFrequency[polymerString[0]] += 1
    letterFrequency[polymerString[-1]] += 1

    # Divide everything by 2
    for key in letterFrequency:
        letterFrequency[key] //= 2

    # Get the max and min values
    letterFrequencyList = sorted(letterFrequency.values(), reverse=True)
    maxLetterFrequency = letterFrequencyList[0]
    minLetterFrequency = letterFrequencyList[letterFrequencyList.index(0) - 1]

    print(f'Max Letter Frequency: {maxLetterFrequency}')
    print(f'Min Letter Frequency: {minLetterFrequency}')
    print(f'Frequency Spread: {maxLetterFrequency - minLetterFrequency}')

# --- MAIN CODE --- #
isSample = False
numSteps = 40
# part1(isSample, numSteps)
part2(isSample, numSteps)