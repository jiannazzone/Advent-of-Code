import re
from pprint import pprint

# filepath = 'Day03/sample.txt'
# filepath = 'Day03/sample2.txt'
filepath = 'Day03/input.txt'

with open(filepath, 'r') as f:
    data = f.read()

# Part 1
def part1():
    allMults = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    multSum = 0
    for mult in allMults:
        nums = [int(x) for x in mult[4:-1].split(',')]
        multSum += nums[0] * nums[1]
    print(f'Multiplication Sum: {multSum}')

# part1()

# Part 2
def part2():
    allInstructions = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', data)
    addFlag = True
    multSum = 0
    for instruction in allInstructions:
        if instruction == 'do()':
            addFlag = True
        elif instruction == 'don\'t()':
            addFlag = False
        elif addFlag:
            nums = [int(x) for x in instruction[4:-1].split(',')]
            multSum += nums[0] * nums[1]
    print(f'Multiplication Sum: {multSum}')

part2()