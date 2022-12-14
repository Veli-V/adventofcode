#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
data = [d.split("->") for d in data]

cave = {}

def addCoord(x, y):
    return [x[0]+y[0], x[1]+y[1]]
miny, minx = 700, 700
maxy, maxx = 0, 0
for d in data:
    for i in range(1, len(d)):
        start = d[i-1].split(",")
        end = d[i].split(",")
        start = [int(s) for s in start]
        end = [int(e) for e in end]
        #print("27 s:{}, e:{}".format(start, end))
        minx = min(minx, start[0], end[0])
        miny = min(miny, start[1], end[1])
        maxx = max(maxx, start[0], end[0])
        maxy = max(maxy, start[1], end[1])
        if start[1] == end[1]:
            #print("eka kasvaa")
            if start[0] < end[0]:
                for j in range(start[0], end[0]+1):
                    cave[(j, start[1])] = '#'
            else:
                for j in range(end[0], start[0]+1):
                    cave[(j, start[1])] = '#'
        elif start[0] == end[0]:
            #print("Toka kasvaa")
            if start[1] < end[1]:
                for j in range(start[1], end[1]+1):
                    cave[(start[0], j)] = '#'
            else:
                for j in range(end[1], start[1]+1):
                    cave[(start[0], j)] = '#'

            #print(max(start[1], end[1]))
            #print(min(start[1], end[1]))
            for j in range(max(start[1], end[1]), min(start[1], end[1])+dir, dir):
                #print("37:",j)
                cave[(start[0], j)] = '#'


#print(cave)


sand = [500, 0]
lasts = (500,0)
rested = True
falls = [[0,1], [-1,1], [1,1]]
sands = 0
part1 = 0
part1done = False

while rested:
    stillFalling = False
    for f in falls:
        toTest = addCoord(sand, f)
        toTest = (toTest[0], toTest[1])
        if toTest not in cave:
            stillFalling = True
            sand = toTest
            break
    if not stillFalling or sand[1] == maxy+1:
        if part1done == False and sand[1] == maxy+1:
            part1done = True
            part1 = sands
        cave[sand] = "x"
        cave[lasts] = "o"
        lasts = sand
        sands += 1
        sand = (500, 0)
    if cave.get((500,0))== "x": break
    if sand[1] > 200: break



cave[(500,0)] = "S"
print()
for i in range(0, maxy+10):
    print(str(i).zfill(3), end=" ")
    for j in range(minx-10, maxx+10):
        if cave.get((j, i)) == None: print(".", end="")
        else: print(cave.get((j,i)), end="")
    print()

print("Part1:")
print("It dropped {} before going to void".format(part1))
print("Part2:")
print("It dropped {} before blocking start".format(sands))
