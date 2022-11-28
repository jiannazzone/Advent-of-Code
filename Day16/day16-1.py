from pprint import pprint

def generateRules(rawData):
	# Logic to parse the rules
	rulesRaw = rawData[0].splitlines()
	rules = []
	for i in rulesRaw:
		thisRule = i[i.index(':')+2:]
		thisRule = thisRule.split(' or ')
		theseRules = []
		for j in thisRule:
			theseRules.append(tuple([int(x) for x in j.split('-')]))
		rules.append(theseRules)
	return rules
def generateNearbyTickets(rawData):
	nearbyTicketsRaw = rawData[2].splitlines()
	nearbyTickets = []
	for i in nearbyTicketsRaw[1:]:
		thisTicket = [int(x) for x in i.split(',')]
		nearbyTickets.append(thisTicket)
	return nearbyTickets


# Import and clean up the data
rawData = open('sample.txt', 'r').read()
rawData = rawData.split('\n\n')

rules = generateRules(rawData)
nearbyTickets = generateNearbyTickets(rawData)
# Logic to parse yourTicket
# yourTicketRaw = rawData[1].splitlines()
# print('Rules:')
# pprint(rules)
# print('Nearby Tickets:')
# pprint(nearbyTickets)

invalidValues = []
for ticket in nearbyTickets:
	for value in ticket:
		isValid = []
		#Logic for checking each value against all possible fields
		for eachRule in rules:
			lowerA = eachRule[0][0]
			upperA = eachRule[0][1]
			lowerB = eachRule[1][0]
			upperB = eachRule[1][1]
			if ((value >= lowerA and value <= upperA) or
				(value >= lowerB and value <= upperB)):
				isValid.append(True)
			else:
				isValid.append(False)
		# print('Value: ' + str(value) + ' - ' + str(isValid))
		if not any(isValid):
			invalidValues.append(value)

invaludSum = 0
for i in invalidValues:
	invaludSum += i
print('Invalid Values:')
pprint(invalidValues)
print('Invalid Sum: ' + str(invaludSum))
