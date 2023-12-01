# Process puzzle input
examplePath = '2023/Day01/example.txt'
inputPath = '2023/Day01/input.txt'

numsAsText = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# Part 1
def part1():
    with open(inputPath, 'r') as f:
        calibrationData = f.read().splitlines()

    allDigits = []
    for line in calibrationData:
        thisLineDigits = ''
        for char in line:
            if char.isdigit():
                thisLineDigits += char
        allDigits.append(thisLineDigits)

    sum = 0
    for x in allDigits:
        thisNum = int(x[0] + x[-1])
        sum += thisNum
    print(f'Part 1 summation: {sum}')

# Part 2
examplePath2 = '2023/Day01/example2.txt'

def findFirstDigit(line):
    # Start by looking start -> end
    for i in range(len(line)):
        # Check if we have a regular digit
        if line[i].isdigit():
            return line[i]
        else:
            substring = line[0:i+1]
            for key in numsAsText.keys():
                if key in substring:
                    return str(numsAsText[key])

def findLastDigit(line):
    for i in range(len(line)-1,-1,-1):
        # Check if we have a regular digit
        if line[i].isdigit():
            return line[i]
        else:
            substring = line[i:len(line)]
            for key in numsAsText.keys():
                if key in substring:
                    return str(numsAsText[key])

def part2():
    with open(examplePath2, 'r') as f:
        calibrationDataRaw = f.read().splitlines()
    
    calibrationData = []
    for line in calibrationDataRaw:
        thisLineDigits = ''
        thisLineDigits += findFirstDigit(line)
        thisLineDigits += findLastDigit(line)
        calibrationData.append(thisLineDigits)

    sum = 0
    for x in calibrationData:
        thisNum = int(x[0] + x[-1])
        sum += thisNum
    print(f'Part 2 summation: {sum}')

# part1()
part2()