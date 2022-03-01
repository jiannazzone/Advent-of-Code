# Advent of Code 2015-3

filename = '/Users/aiannazzone/Documents/GitHub/Advent-of-Code-2015/Day03/input1.txt'
with open(filename) as f:
    data = f.read()

def deliverPresents(data):
    # Houses will be stored as a dictionary: "x,y":numPresents
    visitedHouses = { "0,0": 1 }

    # Track our locations
    currentX = 0
    currentY = 0

    # Loop through the commands.
    # If the house is new, add it to visitedHouses
    # If the house already exists, add another present
    for step in data:
        # Process the step
        if step == "^":
            currentY += 1
        elif step == "v":
            currentY -= 1
        elif step == ">":
            currentX += 1
        elif step == "<":
            currentX -= 1
        
        # Check to see if the house exists in the dictionary
        if f'{currentX},{currentY}' in visitedHouses.keys():
            visitedHouses[f'{currentX},{currentY}'] += 1
        else:
            visitedHouses[f'{currentX},{currentY}'] = 1
    return visitedHouses

part1 = deliverPresents(data)
print(f'Presents were delivered to {len(part1)} houses.')