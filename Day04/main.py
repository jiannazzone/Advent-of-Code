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

for i in range(1, len(data)):
    thisBoard = []
    for row in data[i].split('\n'):
        if row[0] == ' ':
            row = row[1:]
        row = re.split('  | ', row)
        thisBoard.append([int(x) for x in row])
    boards.append(thisBoard)

def applyNumber(thisNum, theseBoards):
    # Apply number to all bingo boards
    for i in range(0, len(theseBoards)):
        for row in range(0, len(theseBoards[i])):
            for col in range(0, len(theseBoards[i][row])):
                if theseBoards[i][row][col] == thisNum:
                    theseBoards[i][row][col] = 'x'
    return theseBoards

def checkForWin(theseBoards):

    for i in range(0, len(theseBoards)):
        # Check rows
        thisBoard = theseBoards[i]
        for row in thisBoard:
            rowEvaluation = []
            for number in row:
                if number == 'x':
                    rowEvaluation.append(True)
                else:
                    rowEvaluation.append(False)
            if all(rowEvaluation):
                return i
        
        # Check for columns
        for col in range(0, len(thisBoard)):
            columnEvaluation = []
            for row in thisBoard:
                if row[col] == 'x':
                    columnEvaluation.append(True)
                else:
                    columnEvaluation.append(False)
            if all(columnEvaluation):
                return i
    
    # If no winner yet
    return -1

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
    winBoards = boards.copy()
    for number in bingoNumbers:
        winBoards = applyNumber(number, winBoards)
        winningBoard = checkForWin(winBoards)
        if winningBoard > -1:
            print('The winning board was: ' + str(winningBoard))
            getScore(winBoards[winningBoard], number)
            return

def letTheSquidWin():
    squidBoards = boards.copy()
    for number in bingoNumbers:
        squidBoards = applyNumber(number, squidBoards)
        winningBoard = checkForWin(squidBoards)
        if winningBoard > -1:
            if len(squidBoards) == 1:
                getScore(squidBoards[0], number)
                return
            else:
                squidBoards.pop(winningBoard)
    print('You messed up.')

winBoards = boards.copy()
print('Part 1:')
playBingo()

print('\n----------------\n')

print('Part 2:')
letTheSquidWin()