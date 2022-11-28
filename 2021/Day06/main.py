# Day 06

# filepath = 'Day06/sample.txt'
filepath = 'Day06/input.txt'

def prepareFish():
    with open(filepath) as f:
        initialPopulation = [int(x) for x in f.read().split(',')]
    fishCounter = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for fish in initialPopulation:
        fishCounter[fish] += 1
    return fishCounter

def enhancedSimulateGrowth(days):

    for day in range(days):
        # This represents fish that need to loop back to 6
        # And the number of fish being born
        fishAtZero = fishCounter[0]

        for i in range(1,9):
            fishCounter[i-1] = fishCounter[i]
        fishCounter[8] = fishAtZero
        fishCounter[6] += fishAtZero

    totalCount = sum(fishCounter.values())
    
    print('\n----------')
    print('After ' + str(days) + ' days, there are ' + str(totalCount) + ' fish.')
    print('----------\n')

#--- MAIN CODE ---#
daysToSimulate = 256
fishCounter = prepareFish()
enhancedSimulateGrowth(daysToSimulate)