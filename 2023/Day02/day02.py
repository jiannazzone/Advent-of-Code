# Part 1
from pprint import pprint

# Prepare the data
samplePath = '2023/Day02/sample.txt'
inputPath = '2023/Day02/input.txt'

with open(inputPath, 'r') as f:
    rawInput = f.read().splitlines()
    i = 1
    allGames = {}
    for line in rawInput:
        id = int(line.split(':')[0].split(' ')[1])
        rawRounds = [x.split(', ') for x in line.split(': ')[1].split('; ')]

        cleanRounds = []
        for round in rawRounds:
            thisRound = {}
            for colorCount in round:
                color = colorCount.split(' ')[1]
                colorNum = colorCount.split(' ')[0]
                thisRound[color] = int(colorNum)
            cleanRounds.append(thisRound)
        allGames[i] = cleanRounds
        i += 1

'''
allGames = {
    gameNum: game
}
game = [round]
round = {
    red: num,
    blue: num,
    green: num
}
'''

def part1():
    #Given by prompt
    maxValues = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def checkGame(allGames, i):
        for round in allGames[i]:
            for color in round.keys():
                if round[color] > maxValues[color]:
                    return 0
        return i
                
    validGameSum = 0
    for i in allGames.keys():
        validGameSum += checkGame(allGames, i)
    print(f'The sum of valid game IDs is {validGameSum}')