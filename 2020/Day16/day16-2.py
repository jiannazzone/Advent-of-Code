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
def generateValidTickets(nearbyTickets):
	validTickets = []
	for ticket in nearbyTickets:
		ticketIsValid = []
		for value in ticket:
			valueIsValid = []
			#Logic for checking each value against all possible fields
			for eachRule in rules:
				lowerA = eachRule[0][0]
				upperA = eachRule[0][1]
				lowerB = eachRule[1][0]
				upperB = eachRule[1][1]
				if ((value >= lowerA and value <= upperA) or
					(value >= lowerB and value <= upperB)):
					valueIsValid.append(True)
				else:
					valueIsValid.append(False)
			# print('Value: ' + str(value) + ' - ' + str(valueIsValid))
			if any(valueIsValid):
				ticketIsValid.append(True)
			else:
				ticketIsValid.append(False)
		# print(ticketIsValid)
		if all(ticketIsValid):
			validTickets.append(ticket)
	return validTickets
def checkTicket(ticket, ticketIndex, eachRule, eachTicketRuleCheck):
	ticketValue = ticket[ticketIndex]
	lowerA = eachRule[0][0]
	upperA = eachRule[0][1]
	lowerB = eachRule[1][0]
	upperB = eachRule[1][1]
	if ((ticketValue >= lowerA and ticketValue <= upperA) or
		(ticketValue >= lowerB and ticketValue <= upperB)):
		eachTicketRuleCheck.append(True)
	else:
		eachTicketRuleCheck.append(False)
	return(eachTicketRuleCheck)
def checkRules(ruleIndex, ticketIndex):
	while True:
		eachTicketRuleCheck = []
		for ticket in validTickets:
			checkTicket(ticket, ticketIndex, rules[ruleIndex], eachTicketRuleCheck)
		if all(eachTicketRuleCheck):
			ticketToRuleMap.append(ticketIndex)
			return ticketToRuleMap
			break
		else:
			ticketIndex += 1

# Import and clean up the data
rawData = open('input.txt', 'r').read()
rawData = rawData.split('\n\n')

rules = generateRules(rawData)
nearbyTickets = generateNearbyTickets(rawData)
validTickets = generateValidTickets(nearbyTickets)
print('Rules:')
pprint(rules)
print('Valid Tickets:')
pprint(validTickets)

# Index of this list represent the index of the tickets
# The value represents the index that it matches in the rules
ticketToRuleMap = []

ticketIndex = 0
for ruleIndex in range(len(rules)):
	ticketToRuleMap = checkRules(ruleIndex, ticketIndex)
print(ticketToRuleMap)