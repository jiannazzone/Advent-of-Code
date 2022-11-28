from pprint import pprint
import string

def countAlphabet(x):
	# Create list of zeros with a spot for each letter of the alphabet
	thisGroup = [n*0 for n in range(len(allQuestions))]
	# Count the number of times that each letter in the alphabet occurs in the group
	for i in range(len(allQuestions)):
		for j in x:
			if allQuestions[i] in j:
				thisGroup[i] += 1
	return thisGroup

# Import list of all alphabet
allQuestions = list(string.ascii_lowercase)

# Import text file and clean up
rawData = open('./input.txt', 'r').read().replace('\n\n', '-').split('-')

# Reformat so that each group is its own list
formattedData = []
for i in rawData:
	formattedData.append(i.split('\n'))

# Create a list of zeroes representing each of the groups
questionCount = [n*0 for n in range(len(formattedData))]

for i in range(len(formattedData)):
	# Get total number of times that each letter occurs in the group
	thisGroup = countAlphabet(formattedData[i])

	# If the occurences for a letter == number of people in the group
	# Add one to the question count for that group
	for j in thisGroup:
		if j == len(formattedData[i]):
			questionCount[i] += 1

# Sum all of the question counts for the final tally
finalSum = 0
for i in questionCount:
	finalSum += i

print('The final sum is ' + str(finalSum))