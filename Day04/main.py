# Day 04
from pprint import pprint
import re

filepath = 'Day04/sample.txt'
# filepath = 'Day04/input.txt'

with open(filepath) as f:
    data = f.read().split('\n\n')

# Prepare the Boards and Bingo Numbers
bingoNumbers = data[0]
calledNumbers = []
boards = []

for i in range(1, len(data)):
    thisBoard = []
    for row in data[i].split('\n'):
        if row[0] == ' ':
            row = row[1:]
        row = re.split('  | ', row)
        thisBoard.append(row)
    boards.append(thisBoard)

def checkForWin(boards, calledNumbers):
    pass

def playBingo(boards, bingoNumbers, calledNumbers):
    pass