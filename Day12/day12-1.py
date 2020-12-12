from pprint import pprint

def moveForward(x, y, direction, moveDistance):
	if direction == 'E':
		x += moveDistance
	elif direction == 'W':
		x -= moveDistance
	elif direction == 'N':
		y += moveDistance
	else:
		y -= moveDistance
	return (x, y)
def turnShip(direction, turnDirection, thisAngle):
	allDirections = ['N', 'E', 'S', 'W']
	thisIndex = allDirections.index(direction)
	if turnDirection == 'R':
		steps = int(thisAngle/90)
		return allDirections[(thisIndex + steps) % 4]
	else:
		steps = -int(thisAngle/90)
		return allDirections[(thisIndex + steps) % 4]
def moveShipCardinal(x, y, moveDirection, moveDistance):
	if moveDirection == 'N':
		y += moveDistance
	elif moveDirection == 'S':
		y -= moveDistance
	elif moveDirection =='E':
		x += moveDistance
	else:
		x -= moveDistance
	return (x, y)

# Parse input data
data = open('input.txt', 'r').read().splitlines()
commands = []
for i in data:
	commands.append((i[0], int(i[1:])))

# Prep for iteration
x = 0
y = 0
direction = 'E'

# Execute commands
for i in commands:
	if i[0] == 'F':
		(x, y) = moveForward(x, y, direction, i[1])
	elif i[0] == 'R' or i[0] == 'L':
		direction = turnShip(direction, i[0], i[1])
	else:
		(x, y) = moveShipCardinal(x, y, i[0], i[1])

print('x: ' + str(x))
print('y: ' + str(y))
manhattanDistance = abs(x) + abs(y)
print('Manhattan Distance: ' + str(manhattanDistance))