#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
# PART one
for i in data :
    for j in data:
        if int(i) + int(j) == 2020 :
            print("part1: luvut on " + j + " ja " + i)
            tulo = int(j) * int(i)
            print("part1: niiden tulo= " + str(tulo))

for i in data :
    for j in data:
        for k in data:
            if int(i) + int(j) + int(k) == 2020 :
                print("part2: luvut on " + j + ", " + k + " ja " + i)
                tulo = int(j) * int(i) * int(k)
                print("part2: niiden tulo= " + str(tulo))
