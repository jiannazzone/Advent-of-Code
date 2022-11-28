# Day 3

from pprint import pprint

# filepath = 'Day03/sample.txt'
filepath = 'Day03/input.txt'

with open(filepath) as f:
    data = f.read().split('\n')
dataSize = len(data[0])

# Part 1
def getPowerConsumption():
    gamma = ''
    epsilon = ''
    
    for i in range(dataSize):
        zeroes = 0
        ones = 0

        for line in data:
            # print(line)
            if line[i] == '0':
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    powerComsumption = gamma * epsilon

    print('Gamma: ' + str(gamma))
    print('Epsilon: ' + str(epsilon))
    print('Power Consumption: ' + str(powerComsumption))

# Part 2
def parseData(data, thisBit, i):
    newData = []
    for line in data:
        if line[i] == thisBit:
            newData.append(line)
    return newData

def findGasValue(data, isOxygen):
    # True for Oxygen
    # False for CO2
    for i in range(dataSize):
        # Figure out the most common bit for this position
        zeroes = 0
        ones = 0
        for line in data:
            if line[i] == '0':
                zeroes += 1
            else:
                ones += 1
        if isOxygen:
            if zeroes > ones:
                thisBit = '0'
            else:
                thisBit = '1'
        else:
            if zeroes > ones:
                thisBit = '1'
            else:
                thisBit = '0'
        if len(data) > 1:
            data = parseData(data, thisBit, i)
    decimalValue = int(data[0], 2)
    return decimalValue

def getLifeSupport(data):
    oxygenData = data
    co2Data = data

    oxygenValue = findGasValue(oxygenData, True)
    print('Oxygen: ' + str(oxygenValue))

    co2Value = findGasValue(co2Data, False)
    print('CO2: ' + str(co2Value))

    print('Life Support Integer: ' + str(oxygenValue*co2Value))
    

# getPowerConsumption()
getLifeSupport(data)