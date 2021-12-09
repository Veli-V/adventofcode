#!/usr/bin/env python3
import sys
import math
import numpy as np

#input_file = 'test_input.txt'
input_file = 'input.txt'


with open(input_file) as f:
    data = f.readlines()

depths = {}
for i in range(len(data)):
    data[i] = data[i].strip()
    for j in range(len(data[0])):
        depths[(i,j)] = int(data[i][j])


def basinSize(key):
    size = {key}
    if depths.get(key, 10) >= 9:
        return {}

    if depths[key] < depths.get(tuple((key[0], key[1]+1)), 10) :
        size.update(basinSize(tuple((key[0], key[1]+1))))
    if depths[key] < depths.get(tuple((key[0], key[1]-1)), 10) :
        size.update(basinSize(tuple((key[0], key[1]-1))))
    if depths[key] < depths.get(tuple((key[0]-1, key[1])), 10) :
        size.update(basinSize(tuple((key[0]-1, key[1]))))
    if depths[key] < depths.get(tuple((key[0]+1, key[1])), 10) :
        size.update(basinSize(tuple((key[0]+1, key[1]))))
    return size


# PART1


ans = 0
shallows = []
for key in depths:
    shallow = True
    if depths[key] >= depths.get(tuple((key[0], key[1]+1)), 10) :
        shallow = False
    elif depths[key] >= depths.get(tuple((key[0], key[1]-1)), 10) :
        shallow = False
    elif depths[key] >= depths.get(tuple((key[0]-1, key[1])), 10) :
        shallow = False
    elif depths[key] >= depths.get(tuple((key[0]+1, key[1])), 10) :
        shallow = False

    if shallow:
        ans += depths[key] +1
        shallows.append(key)

print("Part1: sum of shallow risk levels: {}".format(ans))

ans = 0
maxs = [0, 0, 0]
for s in shallows:
    size = basinSize(s)
    if (len(size) > min(maxs)):
        maxs[maxs.index(min(maxs))] = len(size)


print("Part2: sum of basins: {}".format(np.prod(maxs)))
