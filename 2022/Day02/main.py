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
    
    def playRound(self):
        roundScore = scoreDict[self.myGo]
        if self.theirGo is self.myGo:
            roundScore += 3 # Draw
        elif (self.myGo is 'rock' and self.theirGo is 'scissors') or (self.myGo is 'paper' and self.theirGo is 'rock') or (self.myGo is 'scissors' and self.theirGo is 'paper'):
            roundScore += 6 # Win
        
        print(f'They chose {self.theirGo}. You chose {self.myGo}.')
        print(f'You earned {roundScore} points this round.\n----------\n')
        return roundScore

# Part 1
def part1(instructions):
    myScore = 0
    for line in instructions:
        thisRound = GameRound(line)
        myScore += thisRound.playRound()
    print(f'Your final score is {myScore}.')        

part1(instructions)