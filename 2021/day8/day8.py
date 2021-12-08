#!/usr/bin/env python3
import sys
import math

#input_file = 'test_input.txt'
input_file = 'input.txt'


with open(input_file) as f:
    data = f.readlines()
data = [d.strip() for d in data]

# PART1
ans = 0
for d in data:
    n = d.split("|")[1]
    for k in n.split(" "):
        if len(k) in [2,3,4,7]:
            ans += 1


print("PART1: The amount of numbers found = {}".format(ans))

# PART2

ans = 0
keys = ["", "", "", "", "", "", "", "", "", ""]
for d in data:
    numbers = d.split("|")[1].split(" ")
    del numbers[0]
    clues = d.split("|")[0].split(" ")
    clues.sort(key=len)
    keys = ["", "", "", "", "", "", "", "", "", ""]
#   ['', 'dg', 'deg', 'gbfd', 'bcdef', 'gdbec', 'cgeab', 'gcfade', 'abdefc', 'gbfcde', 'fbecgda']

    keys[1] = sorted(clues[1])
    keys[7] = sorted(clues[2])
    keys[4] = sorted(clues[3])
    keys[8] = sorted(clues[10])

    # Find 2,3,5
    for i in range(4,7):
        # If it contains all the lines from 1, it must be 3
        if 0 not in [c in clues[i] for c in keys[1]]:
            keys[3] = sorted(clues[i])
        # If it contains all lines in 4 that are not in 1, it must be 5
        elif 0 not in [c in clues[i] for c in (set(keys[1]) ^ set(keys[4]))]:
            keys[5] = sorted(clues[i])
        # otherwise it must be 2
        else:
            keys[2] = sorted(clues[i])

    for i in range(7,10):
        # if it does not contain all lines in 1, it must be 6
        if 0 in [c in clues[i] for c in keys[1]]:
            keys[6] = sorted(clues[i])
        # if it contains all the lines in 5, it must be 9
        elif 0 not in [c in clues[i] for c in keys[5]]:
            keys[9] = sorted(clues[i])
        else:
            keys[0] = sorted(clues[i])


    tmp = ""
    for n in numbers:
        tmp += str((keys.index(sorted(n))))
    ans += int(tmp)



print("PART2: The sum of numbers found = {}".format(ans))
