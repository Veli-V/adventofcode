#!/usr/bin/env python3
import sys

input_file = "test.txt"
#input_file = "input.txt"


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
    aset = set()
    a2 = answers.split("\n")
    for a in a2:
        for b in a:
            print(b)
            aset.add(a)
        print(aset)
    allset.discard('')
    #print(allset)
    #print("Sum for this groups is {}".format(len(allset)))
    return len(allset),2

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
