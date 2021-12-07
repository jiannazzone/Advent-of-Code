# Day 07
from pprint import pprint

filepath = 'Day07/sample.txt'
# filepath = 'Day07/input.txt'

with open(filepath) as f:
    crabPositions = [int(x) for x in f.read().split(',')]
