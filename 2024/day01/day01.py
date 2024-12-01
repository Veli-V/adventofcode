#!/usr/bin/env python3
import sys

input_file = 'input.txt'
#input_file = 'test.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

dl, dr = [],[]
for d in data:
    d = d.split()
    dl.append(int(d[0]))
    dr.append(int(d[1]))

#print(dl, dr)
dl.sort()
dr.sort()
#print(dl, dr)

ans = 0
for i in range(len(dl)):
    ans += abs(dl[i] - dr[i])

print("Part1: ", ans)

dl = list(set(dl))

ans = 0
for d in dl:
    ans += d*dr.count(d)
    
print("Part2: ", ans)
