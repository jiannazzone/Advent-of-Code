from pprint import pprint

# Generates a list of valid sums to check against
def generateSums(lowerBound, upperBound):
	allSums = []
	for i in allNums[lowerBound:upperBound]:
		for j in allNums[lowerBound:upperBound]:
			if i != j:
				allSums.append(i+j)
	return (allSums)
# Return the invalid number in cipher and its position
def getInvalidNum(allNums, lowerBound, upperBound):
	for i in allNums[preambleLength:len(allNums)]:
		theseSums = generateSums(lowerBound, upperBound)
		if i not in theseSums:
			# Return invalid number and its index
			return (i, allNums.index(i))
			break
		lowerBound += 1
		upperBound += 1

# Read input, then cast as int
allNums = open('input.txt', 'r').read().splitlines()
allNums = [int(i) for i in allNums]

preambleLength = 25 #set length of preamble
lowerBound = 0
upperBound = preambleLength
(invalidNum, invalidIndex) = getInvalidNum(allNums, lowerBound, upperBound)
print('Invalid Number: ' + str(invalidNum))
print('Index: ' + str(invalidIndex))

innerCounter = 1
for i in allNums[:invalidIndex]:
	thisSum = i
	thisContiguousSet = [i]
	for j in allNums[innerCounter:invalidIndex]:
		thisSum += j
		thisContiguousSet.append(j)
		if thisSum == invalidNum:
			lowest = min(thisContiguousSet)
			biggest = max(thisContiguousSet)
			print('Sum: ' + str(lowest + biggest))
			break
	innerCounter += 1