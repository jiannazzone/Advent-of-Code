# 1.2

from pprint import pprint

debug = False
# filePath = 'Day 01/Sample_1.txt'
filePath = 'Day 01/Input_1.txt'

increases = 0

# Read File
with open(filePath) as f:
    depths = f.read()
    depths = depths.split('\n')
    depths = [int(i) for i in depths]

# Initialize averages list
averages = [depths[0] + depths[1] + depths[2]]

# Generate averages
for i in range(1, len(depths)):
    if i + 2 < len(depths):
        thisWindow = depths[i] + depths[i+1] + depths[i+2]
        averages.append(thisWindow)

if debug:
    print("Depths:\n")
    pprint(depths)
    print("Averages:\n")
    pprint(averages)

for i in range(1, len(averages)):
    if averages[i] > averages[i-1]:
        increases += 1

pprint('Increases: ' + str(increases))