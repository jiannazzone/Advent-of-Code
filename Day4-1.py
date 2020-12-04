from pprint import pprint

noCountryKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
allKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
passportList = []

# Use comments to select the desired filename
#filename = 'sample.txt' #sample given on AdventOfCode
filename = 'input.txt'

# Import and split the passport file
file = open(filename, 'r')
allPassports = file.read()
allPassports = allPassports.split('\n\n')

# Convert strings into a list
# With tuples for each key/value pair
delimiters = [' ', ':']
for i in range(len(allPassports)):
	allPassports[i] = allPassports[i].replace('\n', ' ')
	allPassports[i] = allPassports[i].split(' ')
	for j in range(len(allPassports[i])):
		allPassports[i][j] = tuple(filter(None, allPassports[i][j].split(':')))

# Convert list of tuples in a list with dictionary entries
for i in allPassports:
	passportList.append(dict(i))

# Check how many valie keys are present
# Passport entry is represented by one item in the list passportDict
validPassportNum = 0
keyCount = []
for i in range(len(passportList)):
	keyCount.append(0)
	for key in noCountryKeys:
		if key in passportList[i]:
			keyCount[i] += 1

for i in keyCount:
	if i == len(noCountryKeys):
		validPassportNum += 1
print(validPassportNum)
