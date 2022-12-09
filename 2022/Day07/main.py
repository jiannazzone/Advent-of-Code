# Day 7
from pprint import pprint

class Directory:
    def __init__(self, name):
        self.name = name
    def getContents(self):
        pass
    def calculateSize(self):
        pass

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def processInput(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    pprint(data)

filename = 'Day07/sample.txt'
processInput(filename)