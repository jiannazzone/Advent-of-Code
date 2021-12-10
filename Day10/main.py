# Day 10
from pprint import pprint

def prepareData(useSample):
    if useSample:
        filepath = 'Day10/sample.txt'
    else:
        filepath = 'Day10/input.txt'
    with open(filepath) as f:
        data = f.read().split('\n')
    return data

def analyzeLines(data):
    # This function will count each pair of opening/closing tags
    # If for every pair, there are fewer opening than closing, line is incomplete?
    # If for at least one pair, there are more closing than opening, line is corrupt?

    tagDictionaryList = []
    for i in range(len(data)):
        
        # Append new dictionary for each line of data
        tagDictionaryList.append({
            'parentheses': [0, 0],
            'brackets': [0, 0],
            'curlyBrackets': [0, 0],
            'carets': [0, 0]
        })

        # Count each letter in each line
        for letter in data[i]:
            if letter == '(':
                tagDictionaryList[i]['parentheses'][0] += 1
            elif letter == ')':
                tagDictionaryList[i]['parentheses'][1] += 1
            elif letter == '[':
                tagDictionaryList[i]['brackets'][0] += 1
            elif letter == ']':
                tagDictionaryList[i]['brackets'][1] += 1
            elif letter == '{':
                tagDictionaryList[i]['curlyBrackets'][0] += 1
            elif letter == '}':
                tagDictionaryList[i]['curlyBrackets'][1] += 1
            elif letter == '<':
                tagDictionaryList[i]['carets'][0] += 1
            elif letter == '>':
                tagDictionaryList[i]['carets'][1] += 1

        print(f'{data[i]} -- Length: {len(data[i])}')
        pprint(tagDictionaryList[i])
        print('')

data = prepareData(True)
print('')
analyzeLines(data)
