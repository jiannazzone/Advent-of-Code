# Day 04
from os import getsid
from pprint import pprint
import re

# filepath = 'Day04/sample.txt'
# filepath = 'Day04/sample2.txt'
filepath = 'Day04/input.txt'

with open(filepath) as f:
    data = f.read().split('\n\n')

# Prepare the Boards and Bingo Numbers
bingoNumbers = [int(x) for x in data[0].split(',')]
boards = []
winBoards = []

for i in range(1, len(data)):
    thisBoard = []
    for row in data[i].split('\n'):
        if row[0] == ' ':
            row = row[1:]
        row = re.split('  | ', row)
        thisBoard.append([int(x) for x in row])
    boards.append(thisBoard)

def applyNumber(thisNum):
    # Apply number to all bingo boards
    for i in range(0, len(boards)):
        for row in range(0, len(boards[i])):
            for col in range(0, len(boards[i][row])):
                if boards[i][row][col] == thisNum:
                    boards[i][row][col] = 'x'

def checkForWin():

    for i in range(0, len(theseBoards)):
        # Check rows
        thisBoard = theseBoards[i]
        for row in thisBoard:
            count = 0
            for number in row:
                if number == 'x':
                    count += 1
            if count == 5:
                return i
        
        # Check for columns
        for col in range(0, 5):
            count = 0
            for row in thisBoard:
                if row[col] == 'x':
                    count += 1
            if count == 5:
                return i
    
    # If no winner yet
    return -1

def checkForWins():
    winsThisRound = []
    for i in range(0, len(boards)):
        # Check rows
        thisBoard = boards[i]
        for row in thisBoard:
            count = 0
            for number in row:
                if number == 'x':
                    count += 1
            if count == 5:
                winsThisRound.append(i)
        
        # Check for columns
        for col in range(0, 5):
            count = 0
            for row in thisBoard:
                if row[col] == 'x':
                    count += 1
            if count == 5:
                winsThisRound.append(i)
    return winsThisRound

def getScore(board, lastNum):
    unmarkedSum = 0
    for row in board:
        for num in row:
            if num != 'x':
                unmarkedSum += num
    score = unmarkedSum * lastNum
    print('Sum: ' + str(unmarkedSum))
    print('Final Number: ' + str(lastNum))
    print('Final Score: ' + str(score))

def playBingo():
    winBoards = list(boards)
    for number in bingoNumbers:
        winBoards = applyNumber(number, winBoards)
        winningBoard = checkForWin(winBoards)
        if winningBoard > -1:
            print('The winning board was: ' + str(winningBoard))
            getScore(winBoards[winningBoard], number)
            return

def letTheSquidWin():
    
    for number in bingoNumbers:
        applyNumber(number)
        winsThisRound = sorted(checkForWins(), reverse=True)

        # Wait until the 5th number to start checking
        if bingoNumbers[4] != number:
            if len(boards) > 1 and len(winsThisRound) > 0:
                for i in winsThisRound:
                    del boards[i]
            elif len(winsThisRound) == 1:
                getScore(boards[0], number)
                return
    print('You messed up.')
        

# print('Part 1:')
# playBingo()

print('\n----------------\n')

print('Part 2:')
letTheSquidWin()