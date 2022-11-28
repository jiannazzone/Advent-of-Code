from pprint import pprint

def moveForward(moveNum, waypoint, ship):
	ship[0] += waypoint[0]*moveNum
	ship[1] += waypoint[1]*moveNum
	return ship
def rotateWayPoint(direction, degrees, waypoint):
	if degrees >= 360:
		degrees = degrees % 360
	if direction == 'L':
		degrees = 360 - degrees
	
	# Turning Logic
	if degrees == 90:
		x = waypoint[1]
		y = -waypoint[0]
	elif degrees == 180:
		x = -waypoint[0]
		y = -waypoint[1]
	elif degrees == 270:
		x = -waypoint[1]
		y = waypoint[0]
	newWaypoint = [x, y]
	return newWaypoint
def moveWaypoint(direction, distance, waypoint):
	if direction == 'N':
		waypoint[1] += distance
	elif direction == 'S':
		waypoint[1] -= distance
	elif direction == 'E':
		waypoint[0] += distance
	else:
		waypoint[0] -= distance
	return waypoint

# Parse input data
data = open('input.txt', 'r').read().splitlines()
commands = []
for i in data:
	commands.append((i[0], int(i[1:])))

waypoint = [10, 1]
ship = [0, 0]

for i in commands:
	if i[0] == 'F':
		ship = moveForward(i[1], waypoint, ship)
	elif i[0] == 'L' or i[0] =='R':
		waypoint = rotateWayPoint(i[0], i[1], waypoint)
	else:
		waypoint = moveWaypoint(i[0], i[1], waypoint)

print('x: ' + str(ship[0]))
print('y: ' + str(ship[1]))
manhattanDistance = abs(ship[0]) + abs(ship[1])
print('Manhattan Distance: ' + str(manhattanDistance))