import string

def removeDuplicates(x):
	noDuplicates = ''
	for i in x:
		for j in i:
			if j not in noDuplicates:
				noDuplicates += j
	return noDuplicates

# Import list of all alphabet
allQuestions = list(string.ascii_lowercase)

# Import text file and clean up
rawData = open('./input.txt', 'r').read().replace('\n\n', '-').split('-')

# Reformat so that each group is its own list
formattedData = []
for i in rawData:
	formattedData.append(i.split('\n'))

questionCount = [] # Number of questions that each group answered

# Loop through each group and count the number of questions
# Using the removeDuplicates function
# Append the length of that string to the list
# The length of the string represents the number of questions
# That they answered
for i in formattedData:
	questionCount.append(len(removeDuplicates(i)))

# Loop through the questionCount and get the sum of all numbers
questionSum = 0
for i in questionCount:
	questionSum += i

print('The sum is ' + str(questionSum))