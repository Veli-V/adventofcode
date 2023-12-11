#!/usr/bin/env python3
import sys
import math

input_file = "test.txt"
#input_file = 'input.txt'


if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

#for d in data:
    #print(d)

i = 0
while i < len(data):
    if "#" not in data[i]:
        data.insert(i, data[i])
        i += 1
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
        for j in range(len(data)):
            str = data[j]
            str = str[:i] + "." + str[i:]
            data[j] = str
        i += 1
    i += 1

#print(" ")
#for d in data:
    #print(d)

def countDistance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

galaxies = []

for idd, d in enumerate(data):
    for idc, c in enumerate(d):
        if c == "#":
            galaxies.append([idd, idc])

print(galaxies)
ans = 0
for idg, g in enumerate(galaxies):
    for i in range(idg, len(galaxies)):
        ans += countDistance(g, galaxies[i])


print("Part1: ", ans)
