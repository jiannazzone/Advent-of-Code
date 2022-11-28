from pprint import pprint

# Generates a list of valid sums to check against
def generateSums(lowerBound, upperBound):
	allSums = []
	for i in allNums[lowerBound:upperBound]:
		for j in allNums[lowerBound:upperBound]:
			if i != j:
				allSums.append(i+j)
	return (allSums)


# Read input, then cast as int
allNums = open('input.txt', 'r').read().splitlines()
allNums = [int(i) for i in allNums]

preambleLength = 25 #set length of preamble
lowerBound = 0
upperBound = preambleLength

for i in allNums[preambleLength:len(allNums)]:
	theseSums = generateSums(lowerBound, upperBound)
	if i not in theseSums:
		print(str(i) + ': Invalid')
		break
	lowerBound += 1
	upperBound += 1