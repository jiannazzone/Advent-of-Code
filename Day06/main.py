# Day 06
from pprint import pprint

filepath = 'Day06/sample.txt'
# filepath = 'Day06/input.txt'

class Lanternfish:
    def __init__(self, age, firstTime):
        self.age = age
        self.firstTime = firstTime

allFish = []

def prepareFish():
    with open(filepath) as f:
        initialPopulation = [int(x) for x in f.read().split(',')]
    for age in initialPopulation:
        newFish = Lanternfish(age, False)
        allFish.append(newFish)

def simulateGrowth(days):

    for i in range(days):

        # Generate a list of newly-born fish for each day
        fishToAppend = []

        # Simulate the age process for already-existing fish
        for fish in allFish:
            fish.age -= 1

            if fish.age < 0:
                fish.age = 6
                fish.firstTime = False
                fishToAppend.append(Lanternfish(8, True))
        
        # Append all newly-born fish
        for fish in fishToAppend:
            allFish.append(fish)
    
    print('After ' + str(days) + ' days, there are ' + str(len(allFish)) + ' fish.')


prepareFish()
print('\n----Part 1----')
simulateGrowth(80)