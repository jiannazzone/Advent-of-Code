#Day 2

def processInput(filename):
    with open(filename) as f:
        data = f.read()
        instructions = [y.split(' ') for y in data.split('\n')]
        return instructions

filename = 'Day02/sample.txt'
instructions = processInput(filename)
print(instructions)