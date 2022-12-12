#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'
sys.setrecursionlimit(20000)

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        x = self.x - other.x
        y = self.y - other.y
        if y >= 0 and x >=0 and x < len(hills) and y < len(hills[0]):
            return Coord(x, y)
        else:
            return None

    def __str__(self):
        return "{}:{}".format(self.x, self.y)
class Hill:
    def __init__(self, char, position):
        self.char = char
        self.height = ord(char)
        self.routeLenght = sys.maxsize
        self.reverseLenght = sys.maxsize
        self.position = Coord(position[0], position[1])
        self.possibleRoutes = []

    def findRoutes(self, routeLenght):
        if self.routeLenght > routeLenght: self.routeLenght = routeLenght
        else: return
        for a in around:
            apos = self.position.add(a)
            if apos is not None:
                if self.height - hills[apos.x][apos.y].height >= -1:
                    self.possibleRoutes.append(hills[apos.x][apos.y])
        #print(self.possibleRoutes)
        while len(self.possibleRoutes) > 0:
            p = self.possibleRoutes.pop(0)
            p.findRoutes(self.routeLenght+1)

    def findRoutesReverse(self, routeLenght):
        if self.char == 'a' and self not in possibleStarts: possibleStarts.append(self)
        if self.reverseLenght > routeLenght: self.reverseLenght = routeLenght
        else: return
        for a in around:
            apos = self.position.add(a)
            if apos is not None:
                if self.height - hills[apos.x][apos.y].height <= 1:
                    self.possibleRoutes.append(hills[apos.x][apos.y])
        while len(self.possibleRoutes) > 0:
            p = self.possibleRoutes.pop(0)
            p.findRoutesReverse(self.reverseLenght+1)



around = [Coord(-1, 0), Coord(1,0), Coord(0, -1), Coord(0, 1)]

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()


data = [d.strip() for d in data]
#print(data)
#for d in data:
#    print(d)

hills, temphills = [], []
for i in range(len(data)):
    temphills.clear()
    for j in range(len(data[i])):
        tmpHill = Hill(data[i][j], [i,j])
        temphills.append(tmpHill)
        if data[i][j] == 'S':
            s = tmpHill
            s.height = ord('a')
        elif data[i][j] == 'E':
            e = tmpHill
            e.height = ord('z')

    hills.append(temphills.copy())

#part 1
s.findRoutes(0)
print("PART1:")
print("shortest route to E {}".format(e.routeLenght))

#part2
possibleStarts = []
e.findRoutesReverse(0)

shortestReverse = None
for p in possibleStarts:
    #print("Checking point {}:{}, with lenght {}".format(p.char, p.position, p.reverseLenght))
    if shortestReverse is None or p.reverseLenght < shortestReverse.reverseLenght:
        shortestReverse = p

print("Part2")
print("Shortest route to end from anywhere is starting from {}:{}, lenght {}".format(shortestReverse.char, shortestReverse.position, shortestReverse.reverseLenght))
