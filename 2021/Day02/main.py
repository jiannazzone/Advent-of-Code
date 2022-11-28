# 2.1

from pprint import pprint

# Read file
# filepath = 'Day02/Sample_1.txt'
filepath = 'Day02/Input_1.txt'
with open(filepath) as f:
    data = f.read().split('\n')

# Sort commands into a list of tuples
commands = []
for line in data:
    thisCommand = line.split(' ')
    commands.append((thisCommand[0], int(thisCommand[1])))

def part1():
    x = 0
    z = 0

    # Parse commands and write to x z
    for command in commands:
        if command[0] == 'forward':
            x += command[1]
        elif command[0] == 'up':
            z -= command[1]
        elif command[0] == 'down':
            z += command[1]

    # Pring result
    print('\n--------------')
    print('Part 1:')
    print('Horizontal: ' + str(x))
    print('Depth: ' + str(z))
    print('Product: ' + str(x * z))
    print('--------------\n')

def part2():
    x = 0
    z = 0
    aim = 0

    for command in commands:
        if command[0] == 'up':
            aim -= command[1]
        elif command[0] == 'down':
            aim += command[1]
        elif command[0] == 'forward':
            x += command[1]
            z += command[1]*aim
    
    # Pring result
    print('\n--------------')
    print('Part 2:')
    print('Horizontal: ' + str(x))
    print('Depth: ' + str(z))
    print('Product: ' + str(x * z))
    print('--------------\n')


part1()
part2()