#!/usr/bin/env python3

import sys
import string
import re

#input_file = "test.txt"
input_file = "test2.txt"
#input_file = "input.txt"


with open(input_file) as f:
    data = f.read()

data = data.split("\n")
bagName = ""
tmpStr = ""
tmpList = []
bdict = {}
#print(data)


def checkContent(bag):
    count = 0
    #print(bag)
    if any(re.search(r"shiny gold", line) for line in bag):
        return 1
    if "shiny gold" in bag:
        return 1
    elif "no other bags." in bag:
        return 0
    else:
        for b in bag:
            ss = b.split()
            key = ss[1] + " " + ss[2]
            count += checkContent(bdict[key])
        if count > 0:
            return 1
        return 0



def checkHowMany(bag):
    print(bag)
    count = 0
    if "no other bags." in bag:
        print("returning {} from {}".format(0, bag))
        return 0
    else:
        for b in bag:
            ss = b.split()
            key = ss[1] + " " + ss[2]
            count += int(ss[0]) * checkHowMany(bdict[key]) + int(ss[0])
        print("returning {} from {}".format(count, bag))
        return count


for d in data:
    #print(d)
    ds = d.split()
    if not ds:
        break
    ids = iter(ds)
    tmpStr = next(ids)
    #bagName += '"{"'
    bagName += tmpStr
    bagName += " "
    bagName += next(ids)
    #bagName += '" : ('

    tmpStr = ""
    for i in ids:
        if i == "bags":
            continue
        elif i == "contain":
            continue
        elif i == "bag":
            continue
        elif i == "bag,":
            continue
        elif i == "bags,":
            continue
        elif i == "bags.":
            continue
        elif i == "bag.":
            continue
        else:
            tmpStr = i + " " + next(ids) + " " + next(ids)
            tmpList.append(tmpStr)
        #else:
            #tmpStr = i + " " + next(ids)
            #tmpList.append(tmpStr)


    #print(tmpList)
    #print(bagName)
    bdict[bagName] = tmpList.copy()
    tmpList.clear()
    bagName = ""

#print(bdict)
fullCount = 0
for b in bdict:
    #print(bdict[b])
    fullCount += checkContent(bdict[b])

print("PART1: Bag can be in {} bags".format(fullCount))

# PART 2
#
fullCount = checkHowMany(bdict["shiny gold"])

print("PART2: you need {} bags".format(fullCount))
