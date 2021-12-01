#!/usr/bin/env python3
import sys
import numpy as np

input_file = "test.txt"
#input_file = "test2.txt"
#input_file = "input.txt"

with open(input_file) as f:
    time = f.readline()
    busses = f.readline()

busses = busses.strip()
busses = busses.split(',')

min = int(time) + 100000
tmp = 0
atime = 0
nb = ""

for b in busses:
    if b == 'x':
        continue
    tmp = int(time) % int(b)
    atime = int(time) - tmp + int(b)
    if atime < min:
        min = atime
        nb = b

answer = (min - int(time)) * int(nb)

print("PART1: first bus is {} at time {} with answe {}".format(nb, min, answer))


xarray = []
yarray = []
aarray = []

for i in range(len(busses)):
    if busses[i] != 'x':
        xarray.append(int(busses[i]))
        yarray.append(i)
        aarray.append(0)

print(xarray)
print(yarray)

npa = np.array([xarray,yarray])
npb = np.array(aarray)

print(npa)
print(npb)

C = np.linalg.lstsq(npa.T, npb)


print(C)
