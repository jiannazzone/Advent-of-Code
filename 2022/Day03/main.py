#  Day 3

def processInput(filename):
    with open(filename) as f:
        data = f.read().split('\n')
    rucksacks = [ (x[:len(x)//2], x[len(x)//2:]) for x in data]
    return data
    

filename = 'Day03/sample.txt'
rucksacks = processInput(filename)
print(rucksacks)