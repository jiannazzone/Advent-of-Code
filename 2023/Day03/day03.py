samplePath = '2023/Day03/sample.txt'
inputPath = '2023/Day03/input.txt'

with open(inputPath, 'r') as f:
    schematic = f.read().splitlines()

# [print(x) for x in schematic]
# print('\n\n')

def checkNum(num, row, startCol, stopCol):
    '''
    Check the following:
    1. Same row:
        a. startCol - 1
        b. startCol + 1
    2. Previous row:
        a. from startCol - 1 --> startCol + 1
    3. Next row:
        a. from startCol - 1 --> startCol + 1
    '''

    # Check same row
    # Check to the left
    if startCol > 0:
        if schematic[row][startCol - 1] != '.':
            return num
    # Check to the right
    if stopCol < len(schematic[row]) - 1:
        if schematic[row][stopCol + 1] != '.':
            return num
    
    # Prepare columns to check
    if startCol > 0:
        tempStartCol = startCol - 1
    else:
        tempStartCol = startCol
    
    if stopCol < len(schematic[row]) - 1:
        tempStopCol = stopCol + 1
    else:
        tempStopCol = stopCol
    
    # Check row above
    if row > 0:
        charsToCheck = schematic[row - 1][tempStartCol:tempStopCol+1]
        for char in charsToCheck:
            if char != '.' and not char.isdigit():
                return num
    
    # Check row below
    if row < len(schematic) - 2:
        charsToCheck = schematic[row + 1][tempStartCol:tempStopCol+1]
        for char in charsToCheck:
            if char != '.' and not char.isdigit():
                return num

    # Number is not a part number
    return 0


sum = 0
for row in range(len(schematic)):
    thisNum = ''
    thisRow = schematic[row]

    # Check to see if we have started a new number
    # Conditions: number on col = 0, non-digit to the left
    thisNum = ''
    startCol = 0
    stopCol = 0

    for col in range(len(thisRow)):
        thisChar = thisRow[col]

        # Concatenate digits
        if thisChar.isdigit():
            thisNum += thisChar

        # Beginning of number
        if thisChar.isdigit() and col == 0:
            # We found a digit in the first column
            startCol = col
        elif thisChar.isdigit() and not thisRow[col-1].isdigit():
            # We found a digit that was preceded by a non-digit
            startCol = col
        
        # End of number
        elif thisChar.isdigit() and col == len(thisRow)-1:
            # We found a digit that stops at the last column
            stopCol = col
            sum += checkNum(int(thisNum), row, startCol, stopCol)
            thisNum = ''
        elif thisChar.isdigit() and not thisRow[col+1].isdigit():
            # The next character is a non-digit, meaning the number has finished
            stopCol = col
            sum += checkNum(int(thisNum), row, startCol, stopCol)
            thisNum = ''

print('\n----------')
print(f'The sum of all part numbers is {sum}')
print('----------\n')