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


part1Sample = 'Day 01/input1.txt'
calorieCount = processInput(part1Sample)
findMostCalories(calorieCount)