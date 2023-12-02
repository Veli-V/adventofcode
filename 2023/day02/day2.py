#!/usr/bin/env python3
import sys

input_file = "test.txt"
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
print(data)

colors = ["red", "green", "blue"]
MAXcolors = [12, 13, 14]
maxfound = [0,0,0]
ans = 0
ans2 = 0
notOk = False

#part1
maxb, maxr, maxg = 0, 0, 0
for d in data:
    d = d.split(":")
    #print(d)
    game = d[0][4:]
    #print(game)
    round = d[1].split(";")
    for r in round:
        r = r.strip()
        #print(r)
        rr = r.split(" ")
        #print(rr)
        i = 0
        while i < len(rr):
            amount = rr[i]
            color = rr[i+1]
            color = color.strip(",")
            colorind = colors.index(color)
            if int(amount) > MAXcolors[colorind]:
               notOk = True
            if int(amount) > maxfound[colorind]:
               maxfound[colorind] = int(amount)
            i += 2
    if notOk == False:
        ans += int(game)
    ans2 += maxfound[0] * maxfound[1] * maxfound[2]
    notOk = False
    maxfound = [0,0,0]

print("Part1: ", ans)
print("Part2: ", ans2)
