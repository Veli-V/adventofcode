#!/usr/bin/env python3

import sys

#input_file = "test.txt"
#input_file = "test2.txt"
input_file = "input.txt"

# 5 for test.txt, 25 for input.txt
preLenght = 25
data = []
with open(input_file) as f:
    for l in f:
        data.append(int(l))

#print(data)
nlist = data[:preLenght]
c = 0
isOk = False
falseNum = 0
#Part 1
for d in data[preLenght:]:
    for n in nlist:
        c = d-n
        if c in nlist:
            isOk = True
            break
    if not isOk:
        print("PART1: Was not ok {}".format(d))
        falseNum = d
        break
    isOk = False
    nlist.pop(0)
    nlist.append(d)

#part 2
clist = []
for d in data:
   clist.append(d)
   while sum(clist) > falseNum:
       clist.pop(0)
   if sum(clist) == falseNum:
       answer = min(clist) + max(clist)
       print("PART2: found it, answer {1} with list {0}".format(clist, answer))
       break

print("done")
