#!/usr/bin/env python3
import sys
from math import lcm

input_file = "test.txt"
#input_file = "test2.txt"
input_file = "test3.txt"
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]
with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
#print(data)

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self):
        return "n:" + self.name + " L:" + self.left + " R:" + self.right
    def __repr__(self):
        return "n:" + self.name + " L:" + self.left + " R:" + self.right


input = data[0]
i = 2
nodes = {}
posNodes = []
while i < len(data):
    name = data[i][:3]
    left = data[i][7:10]
    right = data[i][12:15]
    #print(name, left, right)
    nodes[name] = Node(name, left, right)
    if name[2:] == "A":
        posNodes.append(nodes[name])
    i += 1


# Part1
notFound = True
pos = nodes["AAA"]
i = 0
direction = ""
while notFound:
    direction = input[i%len(input)]
    #print("i: ", i, " dir: ", direction, " pos: ", pos)
    if direction == "L":
        pos = nodes[pos.left]
    else:
        pos = nodes[pos.right]
    if pos.name == "ZZZ":
        notFound = False
    i += 1

print("part1: ", i)

# Part2
#

notFound = True
loopFound = True
i = 0
direction = ""
ans2 = []
for i in range(len(posNodes)):
    ans2.append(0)

for idx, n in enumerate(posNodes):
    notFound = True
    i = 0
    while notFound:
        direction = input[i%len(input)]
        if direction == "L":
            n = nodes[n.left]
        else:
            n = nodes[n.right]
        if n.name[2:] == "Z":
            notFound = False
        i += 1
    ans2[idx] = i

#print(ans2)
ans = lcm(*ans2)
print("part2: ",  ans)
