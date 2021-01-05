#!/usr/bin/env python3
import sys

#input_file = "test.txt"
input_file = "input.txt"


with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
rows = range(128)
seats = range(8)
planeIds = []

def calculateId(boardingPass):
    lr = rows
    ls = seats
    middle = int(len(lr)/2)
    for b in boardingPass:
        middlel = int(len(lr)/2)
        middles = int(len(ls)/2)
        if b == 'F':
            lr = lr[:middlel]
            #print(lr)
        elif b == 'B':
            lr = lr[middlel:]
            #print(lr)
        elif b == 'L':
            ls = ls[:middles]
            #print(ls)
        elif b == 'R':
            ls = ls[middles:]
            #print(ls)
    id = lr[0]*8+ls[0]
    #print("seat is row {} seat {} and it's id {}".format(lr[0], ls[0], id))
    return id


cid = 0
maxId = 0
minId = 9000
for d in data:
    cid = calculateId(d)
    planeIds.append(cid)
    if cid > maxId:
        maxId = cid
    if cid < minId:
        minId = cid

print("PART1: Max id was {}".format(maxId))

allIds = range(minId, maxId)
myIds = set(allIds)-set(planeIds)
print("PART2: My possible seats are {}".format(myIds))
