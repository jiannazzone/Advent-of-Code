from pprint import pprint
import math

# Import data
data = open('sample.txt', 'r').read().splitlines()
busses = data[1].split(',')
busses = [int(x) if x != 'x' else None for x in busses]
# pprint(busses)

maxOffset = len(busses) - 1

busDictionary = {}
for i in busses:
	if i != None:
		busDictionary[i] = [False, busses.index(i)]

t = 1
while True:
	print(t)
	for bus in busDictionary.keys():
		if (t + busDictionary[bus][1]) % bus == 0:
			busDictionary[bus][0] = True
	check = list(busDictionary.items())
	thisCheck = []
	for i in check:
		thisCheck.append(i[1][0])
	if all(thisCheck):
		print(t)
		break
	t += 1

	for bus in busDictionary.keys():
		busDictionary[bus][0] = False