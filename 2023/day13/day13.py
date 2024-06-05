#!/usr/bin/env python3
import sys
import math
import time
import numpy

debug = False
input_file = "test.txt"
input_file = 'input.txt'

ans = 0

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

data = []
tmpList = []

with open(input_file) as f:
    line = f.readline()
    while line:
        if line != "\n":
            tmpList.append(line.strip())
        else:
            data.append(tmpList.copy())
            tmpList.clear()
        line = f.readline()
    data.append(tmpList.copy())
    tmpList.clear()

data2 = []
for d in data:
    #d = [dd.split() for dd in d]
    data2.append([list(dd) for dd in d])

#print(data2)
data = [numpy.array(d) for d in data2]

def checkMirror(data):
    if debug: print(data)
    possibles = list(range(len(data)-1))
    newPossibles = []
    newPossibles2 = []
    checkSmudge = []
    diffsum = 0

    for p in possibles:
        diffsum = 0
        checkSmudge = []
        try:
            for i in range(len(data)):
                #if debug: print("verrataan", p-i, data[p-i],p+i+1, data[p+i+1])
                if p-i < 0 or p+i >= len(data):
                    if debug: print("Meni rajan yli")
                    break
                checkSmudge = data[p-i] == data[p+i+1]
                diffcount = len(checkSmudge) - numpy.count_nonzero(checkSmudge)
                diffsum += diffcount
                #print("count: ", diffcount, " sum: ", diffsum)
                if diffsum > 1:
                    if debug: print("Ei ole peili, diffsum: ", diffsum)
                    break
        except IndexError:
            mirror = True
        if diffsum == 0:
            if debug: print("oli peili", p)
            newPossibles.append(p+1)
        if diffsum == 1:
            if debug: print("oli peili 2", p)
            newPossibles2.append(p+1)
    if debug: print("palautetaan:", newPossibles, newPossibles2)
    newPossibles2 = [p for p in newPossibles2 if p not in newPossibles]
    return newPossibles, newPossibles2


ans, ans2 = 0, 0
tmpAns = []
tmpAns2 = []
tmp2Ans = []
tmp2Ans2 = []
for idd, d in enumerate(data):
    if debug: print("part1")
    tmpAns, tmp2Ans = checkMirror(d)
    d = numpy.transpose(d)
    if debug: print("part2")
    tmpAns2, tmp2Ans2 = checkMirror(d)
    if len(tmpAns) == 0 and len(tmpAns2) == 0:
        print("Molemmat nollia", idd)
    if len(tmp2Ans) == 0 and len(tmp2Ans2) == 0:
        print("Molemmat nollia", idd)
    ans += sum(tmpAns)*100
    ans += sum(tmpAns2)
    ans2 += sum(tmp2Ans)*100
    ans2 += sum(tmp2Ans2)

print("Part1:", ans)
print("Part2:", ans2)
