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

def deliverPresents2(data):
    # Houses will be stored as a dictionary: "x,y":numPresents
    visitedHouses = { "0,0": 1 }
    isSanta = True

    # Track our locations
    santaX = 0
    santaY = 0
    roboX = 0
    roboY = 0

    # Loop through the commands.
    # If the house is new, add it to visitedHouses
    # If the house already exists, add another present
    for step in data:
        # Process the step
        if isSanta:
            if step == "^":
                santaY += 1
            elif step == "v":
                santaY -= 1
            elif step == ">":
                santaX += 1
            elif step == "<":
                santaX -= 1
        else:
            if step == "^":
                roboY += 1
            elif step == "v":
                roboY -= 1
            elif step == ">":
                roboX += 1
            elif step == "<":
                roboX -= 1
        
        # Check to see if the house exists in the dictionary
        if isSanta:
            if f'{santaX},{santaY}' in visitedHouses.keys():
                visitedHouses[f'{santaX},{santaY}'] += 1
            else:
                visitedHouses[f'{santaX},{santaY}'] = 1
        else:
            if f'{roboX},{roboY}' in visitedHouses.keys():
                visitedHouses[f'{roboX},{roboY}'] += 1
            else:
                visitedHouses[f'{roboX},{roboY}'] = 1
        
        # Toggle who is moving
        isSanta = not isSanta

    return visitedHouses

part1 = deliverPresents(data)
print(f'\n-----Part 1:-----\nPresents were delivered to {len(part1)} houses.\n-----------------\n')

part2 = deliverPresents2(data)
print(f'\n-----Part 1:-----\nPresents were delivered to {len(part2)} houses.\n-----------------\n')