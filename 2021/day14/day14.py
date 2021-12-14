#!/usr/bin/env python3

import sys
from collections import defaultdict

input_file = 'test_input.txt'
input_file = 'input.txt'

with open(input_file) as f:
    data = f.readlines()

file = open(input_file, "r")
polymer = file.readline().strip()
polymer = [p for p in polymer]
file.readline()
line = file.readline()
insertions = {}
while line:
    insertions[line.split(" ->")[0]] = line.split("->")[1].strip()
    line = file.readline()
file.close()

rounds = 41

print()

pairs = defaultdict(int)

for i in range(len(polymer)-1):
    pairs[polymer[i] + polymer[i+1]] += 1

partDividers = (10, 40)
for r in range(rounds):
    if r in partDividers:
        elements = defaultdict(int)
        elements[polymer[0]] = 1
        elements[polymer[-1]] = 1
        for p in pairs.keys():
            elements[p[0]] += pairs[p]
            elements[p[1]] += pairs[p]
        print("PART{}: minimi {} ja maksimi {} eli {}".format(partDividers.index(r)+1,min(elements.values())/2, max(elements.values())/2, max(elements.values())/2 - min(elements.values())/2))

    np = defaultdict(int)
    for p in pairs.keys():
        rule = insertions[p]
        np[p[0] + rule] += pairs[p]
        np[rule + p[1]]  += pairs[p]
    pairs = np
