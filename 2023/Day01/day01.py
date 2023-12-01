# Day 1 Part 1

# Process puzzle input
examplePath = '2023/Day01/example.txt'
inputPath = '2023/Day01/input.txt'

with open(inputPath, 'r') as f:
    calibrationData = f.read().splitlines()

allDigits = []
for line in calibrationData:
    thisLineDigits = ''
    for char in line:
        if char.isdigit():
            thisLineDigits += char
    allDigits.append(thisLineDigits)

calibrationNums = []
sum = 0
for x in allDigits:
    thisNum = int(x[0] + x[-1])
    sum += thisNum
    print(thisNum)

print(f'Final summation: {sum}')