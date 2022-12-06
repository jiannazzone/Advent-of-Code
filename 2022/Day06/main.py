# Day 06

sample = open('Day06/sample.txt').read().splitlines()
input = open('Day06/input.txt').read()

def findStartMarker(packet):
    for i in range(3, len(packet)):
        bitSet = {packet[i-3], packet[i-2], packet[i-1], packet[i]}
        if len(bitSet) == 4:
            return i+1

def findStartMessage(packet):
    for i in range(13, len(packet)):
        bitSet = set()
        for j in range(0, 14):
            bitSet.add(packet[i-j])
        if len(bitSet) == 14:
            return i+1

def part1():
    # Test samples
    print('Samples:')
    for line in sample:
        print(findStartMarker(line))
    print('--------------\n')
    
    # Use Input
    print(f'Input: {findStartMarker(input)}')
# part1()

def part2():
    # Test samples
    print('Samples:')
    for line in sample:
        print(findStartMessage(line))
    print('--------------\n')

    # Use Input
    print(f'Input: {findStartMessage(input)}')

part2()