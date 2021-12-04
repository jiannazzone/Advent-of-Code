# Day 04
from pprint import pprint
import re

filepath = 'Day04/sample.txt'
# filepath = 'Day04/input.txt'

with open(filepath) as f:
    data = f.read().split('\n\n')

# Prepare the Boards and Bingo Numbers
bingoNumbers = [int(x) for x in data[0].split(',')]
calledNumbers = []
boards = []

for i in range(1, len(data)):
    thisBoard = []
    for row in data[i].split('\n'):
        if row[0] == ' ':
            row = row[1:]
        row = re.split('  | ', row)
        thisBoard.append([int(x) for x in row])
    boards.append(thisBoard)

def checkForWin():
    for i in range(0, len(boards)):
        # Check rows
        thisBoard = boards[i]
        for row in thisBoard:
            rowEvaluation = []
            for number in row:
                if number in calledNumbers:
                    rowEvaluation.append(True)
                else:
                    rowEvaluation.append(False)
            if all(rowEvaluation):
                return i
        
        # Check for columns
        for col in range(0, len(thisBoard)):
            columnEvaluation = []
            for row in thisBoard:
                if row[col] in calledNumbers:
                    columnEvaluation.append(True)
                else:
                    columnEvaluation.append(False)
            if all(columnEvaluation):
                return i
    
    # If no winner this round
    return -1

def getScore(board):
    unmarkedSum = 0
    for row in board:
        for num in row:
            if num not in calledNumbers:
                unmarkedSum += num
    score = unmarkedSum * calledNumbers[-1]
    print('Sum: ' + str(unmarkedSum))
    print('Final Number: ' + str(calledNumbers[-1]))
    print('Final Score: ' + str(score))

def playBingo():
    for number in bingoNumbers:
        calledNumbers.append(number)
        winningBoard = checkForWin()
        if winningBoard > -1:
            print('Winning board is: ' + str(winningBoard))
            getScore(boards[winningBoard])
            return
    print('You messed up.')

playBingo()