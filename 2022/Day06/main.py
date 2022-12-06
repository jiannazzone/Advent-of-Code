# Day 06

sample = open('Day06/sample.txt').read().splitlines()
input = open('Day06/input.txt').read()

def findStartMarker(packet):
    for i in range(3, len(packet)):
        bitSet = set()
        bitSet.add(packet[i-3])
        bitSet.add(packet[i-2])
        bitSet.add(packet[i-1])
        bitSet.add(packet[i])
        # print(bitSet)
        if len(bitSet) == 4:
            return i+1

def part1():
    # Test samples
    print('Samples:')
    for line in sample:
        print(findStartMarker(line))
    print('--------------\n')
    
    # Use Input
    print(f'Input: {findStartMarker(input)}')

part1()