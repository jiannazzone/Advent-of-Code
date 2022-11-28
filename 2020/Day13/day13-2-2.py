from pprint import pprint
import math

# Import data
data = open('input.txt', 'r').read().splitlines()
busses = data[1].split(',')
busses = [int(x) if x != 'x' else None for x in busses]
# pprint(busses)

offsets = {}
for bus in busses:
	if bus != None:
		offsets[bus] = busses.index(bus)

t = 0
increment = 1
for bus in list(offsets.keys()):
	while True:
		if (t + offsets[bus]) % bus == 0:
			# print('Bus ' + str(bus) + ' departing at ' + str(t))
			increment = math.lcm(increment, bus)
			# print('Increment: ' + str(increment))
			break
		t += increment
print(t)