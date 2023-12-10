#!/usr/bin/env python3
import sys
import math

sys.setrecursionlimit(15000)
#input_file = "test.txt"
input_file = 'input.txt'
#input_file = "test2.txt"


if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
maxHeight = len(data)
maxWidth = len(data[0])

#print(data)
directions = {
    "|":[[1,0],[-1,0]],
    "-":[[0,1],[0,-1]],
    "L":[[-1,0],[0,1]],
    "J":[[-1,0],[0,-1]],
    "7":[[1,0],[0,-1]],
    "F":[[1,0],[0,1]],
    "S":[[0,0],[0,0]],
    ".":[[0,0],[0,0]]
}

class Pipe:
    def __init__(self, char, loc):
        self.char = char
        self.loc = tuple(loc)
        self.left = tuple([loc[0]+directions[char][0][0],loc[1]+directions[char][0][1]])
        self.right = tuple([loc[0]+directions[char][1][0],loc[1]+directions[char][1][1]])
        self.distance = -1

    def __repr__(self):
        return self.char + " loc: " + str(self.loc) + " L: " + str(self.left) + " R: " + str(self.right)

    def getNext(self):
        return tuple([pipes[self.left].char, pipes[self.right].char])


pipes = {}
s = 0

for idd, d in enumerate(data):
    for idc, c in enumerate(d):
        pipes[idd, idc] = Pipe(c, [idd, idc])
        if c == "S":
            s = pipes[idd, idc]



def coordGet(step, nex):
    return tuple([step[0] + nex[0], step[1] + nex[1]])

def findSConnections(s):
    found = 0
    for next in [[1,0], [-1,0], [0,1], [0,-1]]:
        if -1 not in coordGet(s.loc, next):
            if "S" in pipes[coordGet(s.loc, next)].getNext():
                if found == 0:
                    s.left = coordGet(s.loc, next)
                    found += 1
                else:
                    s.right = coordGet(s.loc, next)


def followLoop(pos, lastPos, loop):
    pipe = pipes[pos]
    pipe.distance = loop
    #print(pipe)
    if loop > 2:
        if pipe.left == s.loc or pipe.right == s.loc:
            return loop
    if pipe.left != lastPos:
        return followLoop(pipe.left, pos, loop+1)
    else:
        return followLoop(pipe.right, pos, loop+1)

def checkDown(pipe):
    newLoc = coordGet(pipe.loc, [1,0])
    if newLoc[0] < 0 or newLoc[0] >= len(data):
        return 0
    if newLoc[1] < 0 or newLoc[1] >= len(data[0]):
        return 0
    downPipe = pipes[newLoc]
    if downPipe.distance != 0:
        if downPipe.distance - pipe.distance == 1:
            return 1
        elif downPipe.distance - pipe.distance == -1:
            return -1
        else:
            return 0

    return "up"

#print(s)
findSConnections(s)
#print(s)

lenght = followLoop(s.left, s.loc, 1)

print("Part1: " + str(math.ceil(lenght/2)))


s.distance = 0
counter = 0
pointsEnclosed = 0
#for x in range(len(data)):
    #for y in range(len(data[x])):
        #pipe = pipes[x,y]
        #if pipe.distance != -1:
            #print(str(pipe.distance).ljust(5), end="")
        #else:
            #print(pipe.char.ljust(5), end="")
    #print()
for x in range(len(data)):
    for y in range(len(data[x])):
        pipe = pipes[x,y]
        if pipe.distance == -1:
            if counter != 0:
                #print("I", end='')
                pointsEnclosed += 1
            #else:
                #print(pipe.char, end='')
        elif pipe.distance != -1:
            if checkDown(pipe) == 1:
                counter += 1
                #print("v", end='')
            elif checkDown(pipe) == -1:
                counter -= 1
                #print("^", end='')
            #else:
                #print(pipe.char, end='')
        #else:
            #print(pipes[x,y].char, end='')
    #print("")

print("Part2: ", pointsEnclosed)
