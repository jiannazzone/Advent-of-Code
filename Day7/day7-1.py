from pprint import pprint

def cleanInput(x):
	x = list(map(lambda st: str.replace(st, '.', ''), x))
	x = list(map(lambda st: str.replace(st, 'bags', ''), x))
	x = list(map(lambda st: str.replace(st, 'bag', ''), x))
	x = list(map(lambda st: str.replace(st, '  ', ' '), x))
	x = list(map(lambda st: str.replace(st, ' ,', ','), x))
	return x
def createBag(x):
	thisRule = x.strip().split(' contain ')
	thisRule[1] = thisRule[1].split(', ')
	thisColor = thisRule[0]
	thisContents = []
	if thisRule[1][0] != 'no other':
		for i in thisRule[1]:
			thisContents.append((i[2:], i[0]))
	allRules.append(Bag(thisColor, thisContents))
def checkBag(x):
	for i in range(len(x)):
		if x[i][0] == 'shiny gold':
			return True
		elif x[i] != []:
			return False
		else:
			return False
class Bag:
	def __init__(thisBag, color, contents):
		thisBag.color = color
		thisBag.contents = contents

# Open the file and clean up the text
rawRules = open('sample.txt', 'r').read().splitlines()
rawRules = cleanInput(rawRules)
# pprint(rawRules[0])

allRules = []
for i in rawRules:
	createBag(i)