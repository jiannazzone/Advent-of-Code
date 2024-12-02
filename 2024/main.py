from pprint import pprint
filePath = 'input.txt'

with open(filePath, 'r') as f:
    reports = [list(map(int, line.split(' '))) for line in f.read().splitlines()]

def checkReport(report):

    allIncreasing = all(x<y for x, y in zip(report, report[1:]))
    allDecreasing = all(x>y for x, y in zip(report, report[1:]))

    if not (allIncreasing or allDecreasing):
        return 0

    for i in range(0, len(report) - 1):
        diff = report[i+1] - report[i]

        # difference is out of spec (must be between 1-3)
        isValid = abs(diff)>0 and abs(diff)<4
        if not isValid:
            return 0
    
    # we finished the loop and therefore are valid
    return 1

safeCount = 0
for report in reports:
    safeCount += checkReport(report)

print(f'Safe Reports: {safeCount}')