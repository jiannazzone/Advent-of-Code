# Day 07
from pprint import pprint

# filepath = 'Day07/sample.txt'
filepath = 'Day07/input.txt'

with open(filepath) as f:
    crabPositions = [int(x) for x in f.read().split(',')]

def calculateFuel(targetPosition):
    totalFuel = 0
    for crab in crabPositions:
        fuelUsed = abs(crab - targetPosition)
        totalFuel += fuelUsed
    return totalFuel

def calculateFuel2(targetPosition):
    totalFuel = 0
    for crab in crabPositions:
        difference = abs(crab - targetPosition)
        for i in range(1, difference + 1):
            totalFuel += i
    return totalFuel

# Function for Part 1
def part1():
    maxPos = sorted(crabPositions)[-1]
    
    totalFuel = 0
    bestPosition = 0
    for i in range(maxPos):
        if i == 0:
            totalFuel = calculateFuel(i)
        else:
            thisCheck = calculateFuel(i)
            if thisCheck < totalFuel:
                totalFuel = thisCheck
                bestPosition = i
    
    print(f"Total fuel used to move to position {bestPosition}: {totalFuel}")

def part2():
    maxPos = sorted(crabPositions)[-1]
    
    totalFuel = 0
    bestPosition = 0
    for i in range(maxPos):
        if i == 0:
            totalFuel = calculateFuel2(i)
        else:
            thisCheck = calculateFuel2(i)
            if thisCheck < totalFuel:
                totalFuel = thisCheck
                bestPosition = i
    
    print(f"Total fuel used to move to position {bestPosition}: {totalFuel}")

# part1()
part2()