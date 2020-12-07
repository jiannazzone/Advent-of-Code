from pprint import pprint

def cleanInput(x):
	x = list(map(lambda st: str.replace(st, '.', ''), x))
	x = list(map(lambda st: str.replace(st, 'bags', ''), x))
	x = list(map(lambda st: str.replace(st, 'bag', ''), x))
	x = list(map(lambda st: str.replace(st, '  ', ' '), x))
	x = list(map(lambda st: str.replace(st, ' ,', ','), x))
	return x
def createDict(x):
	thisRule = x.strip().split(' contain ')
	thisRule[1] = thisRule[1].split(', ')

	thisContents = []
	if thisRule[1][0] != 'no other':
		for i in thisRule[1]:
			thisContents.append((i[2:], i[0]))
	thisDict = {
		'color': thisRule[0],
		'contents': thisContents
	}
	return thisDict
def checkBag(x):
	for i in range(len(x)):
		if x[i][0] == 'shiny gold':
			return True
		elif x[i] != []:
			pprint("Check These: " + str(x[i][0]))
		else:
			return False

# Open the file and clean up the text
rawRules = open('sample.txt', 'r').read().splitlines()
rawRules = cleanInput(rawRules)

# Generate list of rules where each
# Rule is a dictionary entry
allRules = []
for i in rawRules:
	allRules.append(createDict(i))

shinyGoldCount = 0
notEmptyCount = 0
pprint(allRules)

for i in range(len(allRules)):
	if checkBag(allRules[i]['contents']):
		shinyGoldCount += 1

print("Shiny Gold Rules: " + str(shinyGoldCount))