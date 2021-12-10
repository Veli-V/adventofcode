#!/usr/bin/env python3
import sys
import queue

#input_file = 'test_input.txt'
input_file = 'input.txt'

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
points = [3, 57, 1197, 25137]
points2 = [1, 2, 3, 4]

with open(input_file) as f:
    data = f.readlines()

ans = 0
ans2 = 0
ans2s = []
oq = queue.LifoQueue()
corrupted = False
for d in data:
    oq.queue.clear()
    corrupted = False
    d = d.strip()
    for c in d:
        if c in openers:
            oq.put(c)
        else:
            oindex = openers.index(oq.get())
            cindex = closers.index(c)
            if oindex != cindex and not corrupted:
                ans += points[cindex]
                corrupted = True
    if not corrupted:
        while not oq.empty():
            oo = oq.get()
            i = openers.index(oo)
            ans2 *= 5
            ans2 += points2[i]
        ans2s.append(ans2)
        ans2 = 0


ans2s.sort()
ans2 = ans2s[int(len(ans2s)/2)]


print("PART1: Pisteitä saatiin: {}".format(ans))
print("PART2: Pisteitä saatiin: {}".format(ans2))
