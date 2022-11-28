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

    return bitsVersion, bitsType, dataString

def parseLiteralString(dataString):
    # Break literal strings into groups of 5 for analysis
    literalString = ''
    bitsStrings = [dataString[i:i+5] for i in range(0, len(dataString), 5)]
    
    # Concatenate substrings (last 4 digits)
    # The final string has a first digit of 0, triggering the return
    for substring in bitsStrings:
        literalString += substring[1:]
        if substring[0] == '0':
            literalValue = int(literalString, 2)
            analyzedStrings = ''.join(bitsStrings[:bitsStrings.index(substring)+1])
            remainingStrings = ''.join(bitsStrings[bitsStrings.index(substring)+1:])
            return literalValue, analyzedStrings, remainingStrings

def parseOperatorString(dataString):
    # packetMode = 0 -> next 15 bits indicate sub-packet length
    # packetMode = 1 -> next 11 bits indicate number of sub-packets
    packetMode = dataString[0]

    if packetMode == '0':
        # Split out the subpackets from the dataString
        subpacketLength = int(dataString[1:16], 2)
        allSubpackets = dataString[16:subpacketLength+16]
        stringToAnalyze = allSubpackets

        # Analyze all of the substrings
        alreadyParsed = ''
        allVersions = []
        allTypes = []
        allData = []
        allValues = []

        while len(alreadyParsed) < subpacketLength:
            # Get the first version and type from the subpacket
            # If the type does not indicate literal: '100',
            # then the remaining data contains additional subpackets

            bitsVersion, bitsType, thisDataString = parseBinaryString(stringToAnalyze)
            allVersions.append(bitsVersion)
            allTypes.append(bitsType)
            allData.append(thisDataString)

            # If the type indicates a literal string '100', get the value
            # There may be additional strings after the literal string, which need to be analyzed
            if bitsType == '100':
                thisValue, analyzedStrings, stringToAnalyze = parseLiteralString(thisDataString)
                allValues.append(thisValue)
            else:
                theseVersions, theseTypes, theseValues = parseOperatorString(thisDataString)
                for (x, y, z) in zip(theseVersions, theseTypes, theseValues):
                    allVersions.append(x)
                    allTypes.append(y)
                    allValues.append(z)
                analyzedStrings = thisDataString
            alreadyParsed += bitsVersion + bitsType + analyzedStrings
        return allVersions, allTypes, allValues
    
    else:
        # Get the number of subpackets
        numSubpackets = int(dataString[1:12], 2)
        allSubpackets = dataString[12:]
        stringToAnalyze = allSubpackets

        alreadyParsed = ''
        allVersions = []
        allTypes = []
        allData = []
        allValues = []

        # Repeat parsing code for numSubpackets
        for i in range(numSubpackets):
            # Get the first version and type from the subpacket
            # If the type does not indicate literal: '100',
            # then the remaining data contains additional subpackets

            bitsVersion, bitsType, thisDataString = parseBinaryString(stringToAnalyze)
            allVersions.append(bitsVersion)
            allTypes.append(bitsType)
            allData.append(thisDataString)

            # If the type indicates a literal string '100', get the value
            # There may be additional strings after the literal string, which need to be analyzed
            if bitsType == '100':
                thisValue, analyzedStrings, stringToAnalyze = parseLiteralString(thisDataString)
                allValues.append(thisValue)
            else:
                theseVersions, theseTypes, theseValues = parseOperatorString(thisDataString)
                for (x, y, z) in zip(theseVersions, theseTypes, theseValues):
                    allVersions.append(x)
                    allTypes.append(y)
                    allValues.append(z)
                analyzedStrings = thisDataString

            alreadyParsed += bitsVersion + bitsType + analyzedStrings
        return allVersions, allTypes, allValues

print('---------------------------')
binaryString = hexToBinary('8A004A801A8002F478')
bitsVersion, bitsType, dataString = parseBinaryString(binaryString)

if bitsType == '100':
    literalValue, analyzedStrings, remainingStrings = parseLiteralString(dataString)
else:
    allVersions, allTypes, allValues = parseOperatorString(dataString)

print('All Versions:')
pprint(allVersions)
print('\nAll Types:')
pprint(allTypes)
print('\nAll Values:')
pprint(allValues)