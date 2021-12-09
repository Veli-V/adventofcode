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

print("PART1: first bus is {} at time {} with answer {}".format(nb, min, answer))
print(busses)

jatka = True
iii = 1
maksimi = 0
positio = 0
bussiloiset = []
idexiloiset = []
for b in busses:
    if b != 'x':
        bussiloiset.append(int(b))
        idexiloiset.append(busses.index(b))


print(bussiloiset)
print(idexiloiset)
kerroin = np.prod(bussiloiset)
print(kerroin)
while jatka:
    aika = iii*kerroin
    toimi = True
    for i in range(len(bussiloiset)):
        if (aika-idexiloiset[i]) % bussiloiset[i] != 0:
            toimi = False
            break
    if toimi:
        print("Toimi")
        print(aika)
        jatka = False

    iii += 1
    if iii == 100000068781:
        jatka = False
