from pprint import pprint
filePath = 'input.txt'

with open(filePath, 'r') as f:
    reports = [list(map(int, line.split(' '))) for line in f.read().splitlines()]


# Part 1
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


# Part 2
def cleanReport(report):
    for i in range(len(report)):
        tempReport = report[:i]+report[i+1:]
        if checkReport(tempReport) == 1:
            return 1
    return 0
        

'''
def checkReportWithDampener(report):

    dampenerReady = True
    # Clean the report
    cleanReport = []
    for i in range(0, len(report)):

        if dampenerReady:



    allIncreasing = all(x<y for x, y in zip(cleanReport, cleanReport[1:]))
    allDecreasing = all(x>y for x, y in zip(cleanReport, cleanReport[1:]))

    if not (allIncreasing or allDecreasing):
        return 0

    for i in range(0, len(cleanReport) - 1):
        diff = cleanReport[i+1] - cleanReport[i]

        # difference is out of spec (must be between 1-3)
        isValid = abs(diff)>0 and abs(diff)<4
        if not isValid:
            return 0
    
    # we finished the loop and therefore are valid
    return 1
'''

safeWithDampenerCount = 0
for report in reports:
    safeWithDampenerCount += cleanReport(report)
print(f'Safe Reports with Dampener: {safeWithDampenerCount}')
