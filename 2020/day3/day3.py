#!/usr/bin/env python3
import sys

input_file = "test3.txt"
#input_file = "input.txt"


with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]


# part1
modulo = len(data[0])
pos = 0
treecount = 0
for d in data:
    if d[pos] == "#":
        treecount += 1
    pos += 3
    pos = pos % modulo

print("Part1: found {} trees".format(treecount))
#
# part2
#


modulo = len(data[0])
pos = 0
treecount = 0
ranges = [[1,1],[3,1],[5,1],[7,1],[1,2]]
endtrees = 1




for r in ranges:
    for i,d in enumerate(data):
        if i % r[1] == 0:
            if d[pos] == "#":
                    treecount += 1
            pos += r[0]
            pos = pos % modulo
    print("part2: for {} found {} trees".format(r, treecount))
    endtrees = endtrees * treecount
    treecount = 0
    pos = 0


print("Part2: in the end, there where {} trees".format(endtrees))


## exmpale print


modulo = len(data[0])
pos = 0
treecount = 0
ranges = [[1,1],[3,1],[5,1],[7,1],[1,2]]
endtrees = 1




for r in ranges:
    for i,d in enumerate(data):
        if i % r[1] == 0:
            if d[pos] == "#":
                    d[pos] = 'x'
                    treecount += 1
            pos += r[0]
            print(d)
            pos = pos % modulo
    print("part2: for {} found {} trees".format(r, treecount))
    endtrees = endtrees * treecount
    treecount = 0
    pos = 0


print("Part2: in the end, there where {} trees".format(endtrees))
