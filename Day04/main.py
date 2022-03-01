# Advent of Code 2015 Day 4
import hashlib

sampleCodes = ['abcdef', 'pqrstuv']
secretCode = 'ckczppom'

def findKeySuffix(codePrefix):
    currentNum = 0
    
    while True:
        thisCode = f'{codePrefix}{currentNum}'
        hashResult = hashlib.md5(thisCode.encode()).hexdigest()
        
        # Check if we've found a hash with 5 leading zeroes
        if hashResult[:6] == '000000':
            return currentNum
        else:
            currentNum += 1
        

codeSuffix = findKeySuffix(secretCode)
print(f'\n-----Part 1-----\nYour suffix is: {codeSuffix}\n-----------------\n')