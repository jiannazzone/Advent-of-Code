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

        print(calorieCount)

part1Sample = 'Day 01/sample1.txt'
processInput(part1Sample)
