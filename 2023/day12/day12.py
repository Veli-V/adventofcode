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

for d in data:
    print(d)

def positionsStart(row, numbers):
    cnum = numbers[0]
    pos = 0
    for idc, c, in enumerate(row):
        if c == "?":
            for i in range(idc, len(row)):
                if row[i] != "?":
                    spotLenght = i-idc
                    break
            if spotLenght >= cnum:
                print(row[:idc] + str(cnum)*cnum + row[idc+cnum:])
                if len(numbers) > 1:
                    pos += positions(row[idc+cnum:], numbers[1:], idc+cnum)
    return pos

def positions(row, numbers, intention):
    print(" "*intention + "Tarkistetaan: " + row + " numeroilla " + str(numbers))
    cnum = numbers[0]
    pos = 0
    for idc, c, in enumerate(row):
        if c == "?":
            for i in range(idc, len(row)):
                if row[i] != "?":
                    spotLenght = i-idc
                    break
            if spotLenght >= cnum:
                pos += 1
                print(" "*intention, end="")
                print(row[:idc] + str(cnum)*numbers[0] + row[idc+cnum:])
                if len(numbers) > 1:
                    pos *= positions(row[idc+cnum:], numbers[1:], intention+idc+cnum)
    print(" "*intention + "Returning: ", pos)
    if pos == 0: return 1
    return pos

print()
print()
ans = positionsStart(data[1], [2,1,1])
print()
print("part1:", ans)
