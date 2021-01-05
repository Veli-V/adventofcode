#!/usr/bin/env python3
import sys
import string

#input_file = "test.txt"
input_file = "input.txt"


with open(input_file) as f:
    data = f.read()

data = data.split("\n\n")
#print(data)

def countGroup(answers):
    allset = set()
    part2set = set()
    #print(answers)
    answers = answers.strip(' \t\n\r')
    #print(answers)
    for a in answers:
        a = a.strip()
        #print("nyt on {} ja allset {}".format(a, allset))
        allset.add(a)
    # PART 2
    listOfSets = []
    aset = set()
    for c in string.ascii_lowercase:
        aset.add(c)
    #print(aset)

    bset = []
    a2 = answers.split("\n")
    #print("part 2 with {}".format(a2))
    for a in a2:
        for b in a:
            #print(b)
            bset.append(b)
        #print("bset is {}".format(bset))
        listOfSets.append(set(bset))
        bset.clear()
        #print("aset is {}".format(aset))
    for l in listOfSets:
        #print("l is {}".format(l))
        aset = aset.intersection(l)
    #print("After thingies aset is {}".format(aset))
    allset.discard('')
    #print(allset)
    #print("Sum for this groups is {}".format(len(allset)))
    return len(allset),len(aset)

count = 0
count2 = 0
r1 = 0
r2 = 0
for d in data:
    r1, r2  = countGroup(d)
    count += r1
    count2 += r2

print("PART1: Sum of all is {}".format(count))
print("PART2: Sum of all is {}".format(count2))
