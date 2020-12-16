#!/usr/bin/env python3

import sys
#from treelib import Node, Tree

#input_file = "test.txt"
#input_file = "test2.txt"
input_file = "input.txt"

# 5 for test.txt, 25 for input.txt
data = []
tmpList = []
with open(input_file) as f:
    for l in f:
        l = l.strip()
        for c in l:
            tmpList.append(c)
        data.append(tmpList.copy())
        tmpList.clear()

def printData():
    for d in data:
        for c in d:
            print(c + ' ', end="")
        print()

def checkSeats(i,j):
    count = 0

    #Upper row
    if i-1 >= 0 and data[i-1][j] == "#":
        count += 1
    if i-1 >= 0 and j-1 >= 0 and data[i-1][j-1] == "#":
        count += 1
    if i-1 >= 0 and j+1 < len(data[i]) and data[i-1][j+1] == "#":
        count += 1

    #same row
    if j-1 >= 0 and data[i][j-1] == "#":
        count += 1
    if j+1 < len(data[i]) and data[i][j+1] == "#":
        count += 1

    #next row
    if i+1 < len(data) and data[i+1][j] == "#":
        count += 1
    if i+1 < len(data) and j+1 < len(data[i]) and data[i+1][j+1] == "#":
        count += 1
    if i+1 < len(data) and j-1 >= 0 and data[i+1][j-1] == "#":
        count += 1

    return count

def checkSeats2(i,j):
    count = 0
    # Main lines

    # i
    for x in range(1, len(data)):
        if i-x < 0:
            break
        elif data[i-x][j] == '#':
            count += 1
            break
        elif data[i-x][j] == 'L':
            break
    for x in range(1, len(data)):
        if i+x >= len(data):
            break
        elif data[i+x][j] == '#':
            count += 1
            break
        elif data[i+x][j] == 'L':
            break
    # j
    for x in range(1, len(data)):
        if j-x < 0:
            break
        elif data[i][j-x] == '#':
            count += 1
            break
        elif data[i][j-x] == 'L':
            break
    for x in range(1, len(data)):
        if j+x >= len(data[i]):
            break
        elif data[i][j+x] == '#':
            count += 1
            break
        elif data[i][j+x] == 'L':
            break

    #diagonals:
    for x in range(1, len(data)):
        if j-x < 0 or i-x < 0:
            break
        elif data[i-x][j-x] == '#':
            count += 1
            break
        elif data[i-x][j-x] == 'L':
            break
    for x in range(1, len(data)):
        if j-x < 0 or i+x >= len(data):
            break
        elif data[i+x][j-x] == '#':
            count += 1
            break
        elif data[i+x][j-x] == 'L':
            break
    for x in range(1, len(data)):
        if j+x >= len(data[i]) or i+x >= len(data):
            break
        elif data[i+x][j+x] == '#':
            count += 1
            break
        elif data[i+x][j+x] == 'L':
            break
    for x in range(1, len(data)):
        if j+x >= len(data[i]) or i-x < 0:
            break
        elif data[i-x][j+x] == '#':
            count += 1
            break
        elif data[i-x][j+x] == 'L':
            break

    return count


def changePlaces():
    changed = False
    tmpD = [[]] * len(data)
    for i in range(len(data)):
        tmpD[i] = ['.'] * len(data[i])
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'L':
                if checkSeats(i,j) == 0:
                    tmpD[i][j] = '#'
                    changed = True
                else:
                    tmpD[i][j] = "L"
            elif data[i][j] == '#':
                if checkSeats(i,j) >= 4:
                    tmpD[i][j] = 'L'
                    changed = True
                else:
                    tmpD[i][j] = "#"

    return tmpD.copy(), changed

def changePlaces2():
    changed = False
    tmpD = [[]] * len(data)
    for i in range(len(data)):
        tmpD[i] = ['.'] * len(data[i])
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'L':
                if checkSeats2(i,j) == 0:
                    tmpD[i][j] = '#'
                    changed = True
                else:
                    tmpD[i][j] = "L"
            elif data[i][j] == '#':
                if checkSeats2(i,j) >= 5:
                    tmpD[i][j] = 'L'
                    changed = True
                else:
                    tmpD[i][j] = "#"

    return tmpD.copy(), changed

changed = True
while changed:
    data, changed = changePlaces()
#printData()

occupiedSeats = 0
for d in data:
    occupiedSeats += d.count("#")
print("part1: There are {} occupied seats".format(occupiedSeats))

# part 2
data.clear()
tmpList.clear()
with open(input_file) as f:
    for l in f:
        l = l.strip()
        for c in l:
            tmpList.append(c)
        data.append(tmpList.copy())
        tmpList.clear()
changed = True
while changed:
    data, changed = changePlaces2()
    #print()
    #printData()
#printData()

occupiedSeats = 0
for d in data:
    occupiedSeats += d.count("#")
print("part2: There are {} occupied seats".format(occupiedSeats))
