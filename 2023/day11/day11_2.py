#!/usr/bin/env python3
import sys
import math

input_file = "test.txt"
input_file = 'input.txt'

part2Growth = 1000000


if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

#for d in data:
    #print(d)

galaxies = []

for idd, d in enumerate(data):
    for idc, c in enumerate(d):
        if c == "#":
            galaxies.append([idd, idc])

g1 = galaxies.copy()
g2 = galaxies.copy()

def addX1(g):
    return [g[0]+ 1, g[1]]
def addX2(g):
    return [g[0]+ part2Growth-1, g[1]]
def addY1(g):
    return [g[0], g[1]+1]
def addY2(g):
    return [g[0], g[1]+ part2Growth-1]
def countDistance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

i = 0
while i < len(data):
    if "#" not in data[i]:
        for idg, g in enumerate(galaxies):
            if g[0] > i:
                g1[idg] = addX1(g1[idg])
                g2[idg] = addX2(g2[idg])
    i += 1

#print(" ")
#for d in data:
    #print(d)

i = 0
found = False
while i < len(data[0]):
    j = 0
    found = False
    while j < len(data):
        if data[j][i] == "#":
            found = True
            break
        else:
            j += 1
    if not found:
        for idg, g in enumerate(galaxies):
            if g[1] > i:
                g1[idg] = addY1(g1[idg])
                g2[idg] = addY2(g2[idg])
    i += 1

#print(" ")
#for d in data:
    #print(d)

print("Galaxit:")
print(galaxies)
print(g1)
print(g2)
ans = 0
ans2 = 0
for idg, g in enumerate(g1):
    for i in range(idg, len(g1)):
        ans += countDistance(g, g1[i])
for idg, g in enumerate(g2):
    for i in range(idg, len(g2)):
        ans2 += countDistance(g, g2[i])


print("Part1: ", ans)
print("Part2: ", ans2)
