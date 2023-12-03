#!/usr/bin/env python3
import sys

input_file = "test.txt"
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

gears = {}

class Gear:
    def __init__(self,x, y):
        self.name = str(str(x)+","+str(y))
        self.x = x
        self.y = y
        self.numbers = []
    def __str__(self):
        return f"{self.name}({self.numbers})"
    def addNumber(self, number):
        self.numbers.append(number)
    def getNumbers(self):
        return self.numbers


def isSymbol(c):
    if c.isdigit():
        return False
    if c == '.':
        return False
    return True

def checkAround(i, j):
    for x in range(-1,2):
        for y in range(-1,2):
            try:
                if i+x > -1 and j+y > -1:
                    if isSymbol(data[i+x][j+y]):
                        return True
            except:
                pass
    return False

def checkGears(i, j, number):
    for x in range(-1,2):
        for y in range(-1,2):
            try:
                if i+x > -1 and j+y > -1:
                    if data[i+x][j+y] == "*":
                        name = str(str(i+x)+","+str(j+y))
                        #print("tarkistetaan: ", name, " numerolla ", number)
                        if name not in gears:
                            gears[name] = Gear(i+x, j+y)
                            gears[name].addNumber(number)
                        else:
                            gears[name].addNumber(number)
                        return True
            except:
                pass
    return False

#for d in data:
    #print(d)

i,j = 0,0
ans = 0

tempNum = ""

while i < len(data):
    j = 0
    while j < len(data[i]):
        step = data[i][j]
        if step.isdigit():
            tempNum += step
            #print(tempNum)
        elif len(tempNum) != 0:
            #print("Katotaan: ", tempNum, " at:", i, ":", j)
            for x in range(0, len(tempNum)):
                #print("Katotaan", i, ":", j-x-1, " eli: ", data[i][j-x-1])
                if checkAround(i, j-x-1):
                    ans += int(tempNum)
                    checkGears(i, j-x-1, int(tempNum))

                    #print("Oikea numero: ", tempNum)
                    break
            tempNum = ""
        j += 1
    if len(tempNum) != 0:
        #print("Katotaan: ", tempNum, " at:", i, ":", j)
        for x in range(0, len(tempNum)):
            #print("Katotaan", i, ":", j-x-1, " eli: ", data[i][j-x-1])
            if checkAround(i, j-x-1):
                ans += int(tempNum)
                checkGears(i, j-x-1, int(tempNum))
                #print("Oikea numero: ", tempNum)
                break
    tempNum = ""
    i += 1


print("part1: ", ans)
ans = 0
tmpAns = 1

for g in gears:
    #print(g, ":", gears[g].getNumbers())
    if len(gears[g].getNumbers()) == 2:
        for n in gears[g].getNumbers():
            tmpAns *= n
    if tmpAns != 1:
        ans += tmpAns
    tmpAns = 1

print("Part2: ", ans)
