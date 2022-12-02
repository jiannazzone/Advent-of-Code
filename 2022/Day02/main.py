#Day 2

def processInput(filename):
    with open(filename) as f:
        data = f.read()
        instructions = [y.split(' ') for y in data.split('\n')]
        return instructions

filename = 'Day02/input.txt'
instructions = processInput(filename)

choiceDict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

scoreDict = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

class GameRound:
    def __init__(self, playerChoices) -> None:
        self.theirGo = choiceDict[playerChoices[0]]
        self.myGo = choiceDict[choiceDict[playerChoices[1]]]
        self.needToDo = playerChoices[1]
    
    def playRoundPart1(self):
        roundScore = scoreDict[self.myGo]
        if self.theirGo is self.myGo:
            roundScore += 3 # Draw
        elif (self.myGo == 'rock' and self.theirGo == 'scissors') or (self.myGo == 'paper' and self.theirGo == 'rock') or (self.myGo == 'scissors' and self.theirGo == 'paper'):
            roundScore += 6 # Win
        
        # print(f'They chose {self.theirGo}. You chose {self.myGo}.')
        # print(f'You earned {roundScore} points this round.\n----------\n')
        return roundScore

    def playRoundPart2(self):
        roundScore = 0

        if self.needToDo == 'X': #lose
            if self.theirGo == 'rock':
                roundScore = scoreDict['scissors']
            elif self.theirGo == 'paper':
                roundScore = scoreDict['rock']
            else:
                roundScore = scoreDict['paper']

        elif self.needToDo == 'Y': #draw
            myChoice = self.theirGo
            roundScore = 3 + scoreDict[myChoice]

        else: #win
            roundScore = 6
            if self.theirGo == 'rock':
                roundScore += scoreDict['paper']
            elif self.theirGo == 'paper':
                roundScore += scoreDict['scissors']
            else:
                roundScore += scoreDict['rock']
        return roundScore


# Part 1
def part1(instructions):
    myScore = 0
    for line in instructions:
        thisRound = GameRound(line)
        myScore += thisRound.playRoundPart1()
    print(f'Your final score is {myScore}.')
# part1(instructions)

# Part 2
def part2(instructions):
    myScore = 0
    for line in instructions:
        thisRound = GameRound(line)
        myScore += thisRound.playRoundPart2()
    print(f'Your final score is {myScore}.')
part2(instructions)