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

	if thisRule[1][0] == 'no other':
		thisContents = None
	else:
		thisContents = []
		for i in thisRule[1]:
			thisContents.append((i[2:], i[0]))
	thisDict = {
		'color': thisRule[0],
		'isEmpty' : thisRule[1][0] == 'no other',
		'contents': thisContents
	}
	return thisDict

# Open the file and clean up the text
rawRules = open('sample.txt', 'r').read().splitlines()
rawRules = cleanInput(rawRules)

pprint(rawRules)
allRules = []

for i in rawRules:
	allRules.append(createDict(i))