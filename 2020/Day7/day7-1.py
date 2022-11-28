from pprint import pprint

class Bag:
	color = ''
	contents = {}
	foundIn = set()

	def __init__(thisBag, color, contents):
		thisBag.color = color
		thisBag.contents = contents
		thisBag.foundIn = set()
def cleanInput(x):
	x = list(map(lambda st: str.replace(st, '.', ''), x))
	x = list(map(lambda st: str.replace(st, 'bags', ''), x))
	x = list(map(lambda st: str.replace(st, 'bag', ''), x))
	x = list(map(lambda st: str.replace(st, '  ', ' '), x))
	x = list(map(lambda st: str.replace(st, ' ,', ','), x))
	return x
def createBag(x):
	# Clean up data a little bit more
	thisRule = x.strip().split(' contain ')
	thisRule[1] = thisRule[1].split(', ')
	# Get color and contents of the bag
	thisColor = thisRule[0]
	thisContents = {}
	if thisRule[1][0] != 'no other':
		for i in thisRule[1]:
			thisContents[i[2:]] = int(i[0])
	allBags[thisColor] = (Bag(thisColor, thisContents))

def countShiny(x, shinyCount, alreadyChecked):
	for i in x:
		if allBags[i].foundIn != set() and i not in alreadyChecked:
			shinyCount += 1
			alreadyChecked.append(i)
			(shinyCount, alreadyChecked) = countShiny(allBags[i].foundIn, shinyCount, alreadyChecked)
		elif allBags[i].foundIn == set() and i not in alreadyChecked:
			shinyCount += 1
			alreadyChecked.append(i)

	return (shinyCount, alreadyChecked)

# Open the file and clean up the text
rawRules = open('input.txt', 'r').read().splitlines()
rawRules = cleanInput(rawRules)

# Create bag objects for each input line
allBags = {}
for i in rawRules:
	createBag(i)

# Generate set of all bags that
# each bag can be found within
for key in allBags:
	bagObj = allBags[key]
	for color, count in bagObj.contents.items():
		allBags[color].foundIn.add(bagObj.color)

shinyCount = 0
alreadyChecked = []
(shinyCount, alreadyChecked) = countShiny(allBags['shiny gold'].foundIn,
	shinyCount, alreadyChecked)
print('Shiny Count: ' + str(shinyCount))
print('All Checked: ' + str(len(alreadyChecked)))
print('Already Checked: ' + str(alreadyChecked))