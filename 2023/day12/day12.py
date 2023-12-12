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

def positions(row, numbers, intention):
    #print(" "*intention + "Tarkistetaan: " + row + " numeroilla " + str(numbers))
    cnum = numbers[0]
    pos = 0
    spotLenght = 0
    for idc, c, in enumerate(row):
        if c != ".":
            for i in range(idc, len(row)):
                if row[i] == ".":
                    spotLenght = i-idc
                    break
                if i == len(row)-1:
                    spotLenght = i-idc+1
                    break
            if spotLenght >= cnum:
                print(" "*intention, end="")
                print(row[:idc] + str(cnum)*numbers[0] + row[idc+cnum:])
                if len(numbers) > 1:
                    pos += positions(row[idc+cnum+1:], numbers[1:], intention+idc+cnum)
                else:
                    pos += 1
    #print(" "*intention + "Returning: ", pos)
    return pos

print()
print()
ans = 0
tans = 0
#for d in data:
    #row = d.split(" ")
    #print(d, end =": ")
    #tans = positions(row[0],[int(i) for i in row[1].split(",")], 0)
    #print(tans)
    #ans += tans

print(data[2])
row = data[2].split(" ")
ans = positions(row[0],[int(i) for i in row[1].split(",")], 0)
print()
print("part1:", ans)
