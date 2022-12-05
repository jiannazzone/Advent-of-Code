# Day 5
from pprint import pprint

def processInput(filename):
    with open(filename) as f:
        data = f.read().split('\n\n')
    
    # Stacks will be represented as a 2D array, with the last item of each row corresponding to the bottom of the stack
    # [ [stack 1],
    #   [stack 2],
    #   [stack 3], ...
    # ]
    print(data[0] + '\n')
    numStacks = len(data[0].splitlines()[-1].split(' '))//3
    stacks = [[] for x in range(numStacks)]
    for line in data[0].splitlines()[:-1]:
        thisLine = list(line[1:len(line):4])
        for i in range(len(thisLine)):
            stacks[i].append(thisLine[i])

    # For each line of instructions, create a tuple in the format
    # (quantity to move, starting stack, ending stack)
    instructions = []
    for line in data[1].splitlines():
        thisLine = line.split(' ')
        quantity = int(thisLine[1])
        start = int(thisLine[3])
        end = int(thisLine[5])
        instructions.append((quantity, start, end))
    return stacks, instructions

stacks, instructions = processInput('Day05/sample.txt')
pprint(stacks)
pprint(instructions)
