sample = '125 17'
input = '27 10647 103 9 0 5524 4594227 902936'

# stoneList = [int(x) for x in sample.split()]
stoneList = [int(x) for x in input.split()]

# Part 01
def blink():
    newStoneList = []
    for stone in stoneList:
        if stone == 0:
            newStoneList.append(1)
        elif len(str(stone)) % 2 == 0:
            leftStone = str(stone)[:len(str(stone))//2]
            rightStone = str(stone)[len(str(stone))//2:]
            newStoneList.append(int(leftStone))
            newStoneList.append(int(rightStone))
        else:
            newStoneList.append(stone*2024)
    return newStoneList

def part1():
    blinks = 25
    for i in range(blinks):
        stoneList = blink()
    print(len(stoneList))
# part1()

# Part 02