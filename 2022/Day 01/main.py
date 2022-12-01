#Day 1

def processInput(filename):
    with open(filename) as f:
        data = f.read()
        data = data.split('\n\n')
        data = [x.split('\n') for x in data]

        calorieCount = []
        for x in data:
            thisElf = []
            for y in x:
                thisElf.append(int(y))
            calorieCount.append(thisElf)

        return calorieCount
filename = 'Day 01/input1.txt'
calorieCount = processInput(filename)

# Part 1
def findMostCalories(calorieCount):
    maxCalorieIndex = 0
    maxCalorieCount = 0

    # Iterate through each elf and check their calorie sum
    # If the sum is greater than the previous max, update values
    for i in range(len(calorieCount)):
        thisElfCalories = sum(calorieCount[i])
        if thisElfCalories > maxCalorieCount:
            maxCalorieCount = thisElfCalories
            maxCalorieIndex = i
    
    # Now we have iterated through all of the elves and can print out the results
    print(f'The most over-prepared elf is #{maxCalorieIndex + 1} with {maxCalorieCount} calories.')
# findMostCalories(calorieCount)

# Part 2
def findTopThree(calorieCount):
    # Find the sum of all elves
    calorieSums = [sum(x) for x in calorieCount]
    topThreeCalories = sum(sorted(calorieSums)[-3:])
    print(f'The total calories for the top 3 gluttons is {topThreeCalories}.')

findTopThree(calorieCount)