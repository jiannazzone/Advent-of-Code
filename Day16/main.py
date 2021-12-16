# Day 16
from pprint import pprint

hexToBinaryDict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
}
binaryToHexDict = {val: key for key, val in hexToBinaryDict.items()}

def hexToBinary(hexString):
    binaryString = ''
    for char in hexString:
        binaryString += hexToBinaryDict[char]
    return binaryString

def parseBinaryString(binaryString):
    # This will extract the version and type of the packet
    # Version, type, and the remainder will all be returned

    bitsVersion = binaryString[:3]
    bitsType = binaryString[3:6]
    dataString = binaryString[6:]

    print(f'Version: {bitsVersion}')
    print(f'Type: {bitsType}')
    pprint(dataString)

    return bitsVersion, bitsType, dataString

def parseLiteralString(dataString):
    # Break literal strings into groups of 5 for analysis

    literalString = ''
    bitsStrings = [dataString[i:i+5] for i in range(0, len(dataString), 5)]
    print(bitsStrings)
    for substring in bitsStrings:
        literalString += substring[1:]
        if substring[0] == '0':
            return int(literalString, 2)

binaryString = hexToBinary('D2FE28')
bitsVersion, bitsType, dataString = parseBinaryString(binaryString)

if bitsType == '100':
    literalValue = parseLiteralString(dataString)
    print(f'Literal String: {literalValue}')