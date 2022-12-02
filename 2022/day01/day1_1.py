#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
# PART one


cal = 0
cals = []


for d in data:
    if d != '':
        cal += int(d)
    else:
        cals.append(cal)
        cal = 0

print(max(cals))
print(cals.index(max(cals))+1)

top = (sorted(cals, reverse=True))[:3]
print(top)

print(sum(top))
