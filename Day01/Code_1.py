# 1.1
from pprint import pprint

# filePath = 'Day 01/Sample_1.txt'
filePath = 'Day 01/Input_1.txt'

increases = 0

with open(filePath) as f:
    depths = f.read()
    depths = depths.split('\n')
    depths = [int(i) for i in depths]

pprint(depths)

for i in range(len(depths)):
    if i is not 0:
        if depths[i] > depths[i-1]:
            increases += 1

print("Increases: " + str(increases))