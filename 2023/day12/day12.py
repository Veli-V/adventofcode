#!/usr/bin/env python3
import sys
import math
import time
from functools import cache
sys.setrecursionlimit(20000)

input_file = "test.txt"
input_file = 'input.txt'

ans = 0

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

def checkNumbers(row, numbers):
    numbers = [int(i) for i in numbers.split(",")]
    tmpNum = 0
    i = 0
    tmpNumbers = []
    if row.count("#") != sum(numbers):
        return 0
    for r in row:
        if r == "#":
            tmpNum += 1
        elif r == "." and tmpNum != 0:
            if i >= len(numbers):
                return 0
            if tmpNum != numbers[i]:
                return 0
            tmpNumbers.append(tmpNum)
            tmpNum = 0
            i += 1
    if tmpNum != 0:
        tmpNumbers.append(tmpNum)
    if numbers == tmpNumbers:
        return 1
    return 0



    

def createRows(row):
    tmpRow = row
    tmpList = []
    tmpList2 = []

    if len(tmpRow) == 0:
        return tmpList
    elif len(tmpRow) > 1:
        tmpList = createRows(tmpRow[1:])

    if tmpRow[0] == "?":
        if len(tmpList) == 0:
            tmpList2.append(".")
            tmpList2.append("#")
        else:
            for l in tmpList:
                tmpList2.append("."+l)
                tmpList2.append("#"+l)
    else:
        if len(tmpList) == 0:
            tmpList2.append(tmpRow[0])
        for l in tmpList:
            tmpList2.append(tmpRow[0]+l)

    return tmpList2

@cache
def addRows(row1, row2):
    return [row1 + "." + row2, row1 + "#" + row2]


start = time.perf_counter()
tans = 0

#print(dd)
for dd in data:
    #print(dd)
    tans = 0
    row = dd.split(" ")
    nums = row[1]
    row = row[0]
    rows = createRows(row)
    for r in rows:
       tans += checkNumbers(r, nums)
    #print(tans)
    ans += tans
    #ans += len(rows)

end = time.perf_counter()
print("part1:", ans)
print("aikaa meni:",  end-start)
start = time.perf_counter()

#part 2
#Dd = data[1]
#print(dd)
#tans = 0
#row = dd.split(" ")
#nums = row[1]
#nums = nums + "," +nums + "," +nums + "," +nums + "," +nums
#row = row[0]
#row = row + "?" +row + "?" +row + "?" +row + "?" +row
#rows = createRows(row)
#print(len(rows))
#ans += tans
#
#end = time.perf_counter()
#print("part2:", ans)
#print("aikaa meni:",  end-start)
