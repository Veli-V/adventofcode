#!/usr/bin/env python3
import sys
import numpy as np

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

if input_file == 'input.txt':
    testLine = 2000000
    maxcord = 4000000
else:
    testLine = 10
    maxcord = 20

def dist(s, e):
    dist = 0
    if s[0] > e[0]: dist += s[0] - e[0]
    else: dist += e[0] - s[0]
    if s[1] > e[1]: dist += s[1] - e[1]
    else: dist += e[1] - s[1]
    return dist

pairs = []
tmpl = []
dists = []
testMap = {}

for d in data:
    d = d.split(" ")
    tmpl.append(d[2][2:-1])
    tmpl.append(d[3][2:-1])
    tmpl.append(d[8][2:-1])
    tmpl.append(d[9][2:])
    tmpl = [int(t) for t in tmpl]
    pairs.append(tmpl.copy())
    tmpl.clear()

beaconsInLine = {}
for p in pairs:
    disttmp = dist([p[0], p[1]], [p[2], p[3]])
    dists.append([p[0], p[1], disttmp])
    if p[3] == testLine:
        beaconsInLine[p[2], p[3]] = "B"
    rdist = abs(p[1] - testLine)
    rdist = disttmp - rdist
    if rdist > 0:
        for i in range(rdist+1):
            testMap[p[0]+i] = "#"
            testMap[p[0]-i] = "#"


print("Part1:")
print("On line {} there are {} spots where beacon cannot be".format(testLine, len(testMap) - len(beaconsInLine)))

#part2
def checkspot(c):
    for d in dists:
        if dist([d[0], d[1]], [c[0], c[1]]) <= d[2]:
            return False
    return True

for d in dists:
    for i in range(-d[2]-1, d[2]+2):
        n = [d[0]+i, d[1]-i+d[2]+1]
        if n[0] >= 0 and n[0] <= maxcord and n[1] >= 0 and n[1] <= maxcord:
            if checkspot(n):
                print(n)
                print("Löytisi")
                spot = n

print("Part2")
print("Only possible place is {}, with value {}".format(spot, spot[0]*4000000 + spot[1]))
