# Day 06

sample = open('Day06/sample.txt').read().splitlines()
input = open('Day06/input.txt').read()

def findUniqueString(packet, window):
    for i in range(window-1, len(packet)):
        bitSet = set()
        for j in range(0, window):
            bitSet.add(packet[i-j])
        if len(bitSet) == window:
            return i+1

def processStrings(window):
    # Test samples
    sampleString = 'Samples: '
    for line in sample:
        sampleString += f'{findUniqueString(line, window)}, '
    print(sampleString)
    
    # Use Input
    print(f'Input: {findUniqueString(input, window)}')
    print()
processStrings(4)
processStrings(14)