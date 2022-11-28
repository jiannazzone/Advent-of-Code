# Advent of Code 2015

filepath = '/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day01/input1.txt'
with open(filepath) as f:
    instructions = f.read()

# Part 1
floor = 0
for step in instructions:
    if step == '(':
        floor += 1
    else:
        floor -= 1

print(f'The final floor is {floor}')

# Part 2
floor = 0
for i in range(0, len(instructions)):
    if instructions[i] == '(':
        floor += 1
    else:
        floor -= 1

    # Check if we hit the basement
    if floor == -1:
        print(f'The position is: {i + 1}')
        break