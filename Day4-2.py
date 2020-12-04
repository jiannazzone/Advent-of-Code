from pprint import pprint
import string

def validateKeys(thisDict):
	thisDictValidKeys = 0
	# check birthyear
	try:
		int(thisDict['byr'])
	except:
		thisDictValidKeys += 0
	else:
		a = int(thisDict['byr'])
		if a >= 1920 and a <= 2002 and len(str(a)) == 4:
			thisDictValidKeys += 1

	# check issued year
	try:
		int(thisDict['iyr'])
	except:
		thisDictValidKeys += 0
	else:
		a = int(thisDict['iyr'])
		if a >= 2010 and a <= 2020 and len(str(a)) == 4:
			thisDictValidKeys += 1

	# check expiry year
	try:
		int(thisDict['eyr'])
	except:
		thisDictValidKeys += 0
	else:
		a = int(thisDict['eyr'])
		if a >= 2020 and a <= 2030 and len(str(a)) == 4:
			thisDictValidKeys += 1

	# check hgt
	a = str(thisDict['hgt'])
	units = a[-2:]
	try:
		int(a[:-2])
	except:
		thisDictValidKeys += 0
	else:
		digits = int(a[:-2])

		if (digits > 0):
			if units == 'cm' and digits >= 150 and digits <= 193:
				thisDictValidKeys += 1
			elif units == 'in' and digits >= 59 and digits <= 76:
				thisDictValidKeys += 1

	# check hair color
	a = str(thisDict['hcl'])
	if a[0] == '#':
		b = a[1:]
		if all(c in string.hexdigits for c in b):
			thisDictValidKeys += 1

	# check eye color
	a = str(thisDict['ecl'])
	allowedECL = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if a in allowedECL:
		thisDictValidKeys += 1

	# check passport ID
	a = thisDict['pid']
	try:
		int(a)
	except:
		thisDictValidKeys += 0
	else:
		if len(a) == 9 and int(a) > 0:
			thisDictValidKeys += 1

	return thisDictValidKeys

noCountryKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
requiredKeyNum = len(noCountryKeys)
passportList = []
passportsWithAllFields = []

# Use comments to select the desired filename
# filename = 'sample.txt' #sample given on AdventOfCode
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

#delete country ID because who cares?
for i in passportList:
	if 'cid' in i:
		del i['cid']


# If all necessary keys are present, add to list of valid passports
keyCount = 0
for i in range(len(passportList)):
	keyCount = 0
	for key in noCountryKeys:
		if key in passportList[i]:
			keyCount += 1
	if keyCount == requiredKeyNum:
		passportsWithAllFields.append(passportList[i])

print("Passports with all fields filled: " + str(len(passportsWithAllFields)))

# Check each key, see if it meets parameters
totalValidPassports = 0
for i in passportsWithAllFields:
	thisDictValidKeys = validateKeys(i)
	if thisDictValidKeys == 7:
		totalValidPassports += 1
print("Total number of Valid Passports: " + str(totalValidPassports))
