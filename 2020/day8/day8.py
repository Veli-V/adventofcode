#!/usr/bin/env python3

import sys
#import string
#import re

#input_file = "test.txt"
#input_file = "test2.txt"
input_file = "input.txt"


with open(input_file) as f:
    data = f.read().splitlines()

#print(data)
#

def testChange(ci, cvisited, cacc):
    while ci < len(data):
        #print(i)
        #print(data[i])
        dd = data[ci].split()
        if ci in cvisited:
            #print("This command {} is done allready at i={}".format(dd, ci))
            return False
        cvisited.append(ci)
        if dd[0] == "acc":
            cacc += int(dd[1])
            ci += 1
        elif dd[0] == "jmp":
            ci += int(dd[1])
        else:
            ci += 1
    print("PART2: We made it to end, and acc is {}".format(cacc))
    return True

# part 1
acc = 0
visited = []
i = 0
while i < len(data):
    #print(i)
    #print(data[i])
    dd = data[i].split()
    if i in visited:
        print("This command {} is done allready at i={}".format(dd, i))
        print("PART1: acc at this point is {}".format(acc))
        break
    visited.append(i)
    if dd[0] == "acc":
        acc += int(dd[1])
        i += 1
    elif dd[0] == "jmp":
        i += int(dd[1])
    else:
        i += 1


# Part 2

acc = 0
visited.clear()
i = 0


while i < len(data):
    #print(i)
    #print(data[i])
    dd = data[i].split()
    if i in visited:
        print("This command {} is done allready at i={}".format(dd, i))
        print("PART1: acc at this point is {}".format(acc))
        break
    visited.append(i)
    if dd[0] == "acc":
        acc += int(dd[1])
        i += 1
    elif dd[0] == "jmp":
        if testChange(i+1, visited.copy(), acc):
            break
        else:
            i += int(dd[1])
    elif dd[0] == "nop":
        if testChange(i+int(dd[1]), visited.copy(), acc):
            break
        else:
            i += 1
    else:
        i += 1
