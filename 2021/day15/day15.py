#!/usr/bin/env python3

import sys
from queue import PriorityQueue

#input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = 'simple.txt'

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
width = len(data[0])
height = len(data)

def hDist(pos):
    return (width - 1 - pos[0]) + (height - 1 - pos[1])

def inBounds(pos):
    x,y = pos
    if x < 0 or x > width-1 or y < 0 or y > height -1:
        return False
    return True

def neighbors(pos):
    result = []
    x,y = pos
    nn = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for n in nn:
        if inBounds(n):
            result.append(n)
    return result


def findRoute(start, part2 = False):
    global width
    global height
    def cost(pos):
        x, y = pos
        if not part2:
            return positions[pos]
        else:
            result = positions[(x % tilewidth, y % tileheight)] + int(x // tilewidth) + int(y // tileheight)
            if result > 9:
                return result % 9
            else:
                return result
    q = PriorityQueue()
    path = {}
    path[start] = 0
    tilewidth, tileheight = width, height
    if part2:
        width *= 5
        height *= 5
    goal = (width-1, height-1)


    q.put((0, start))

    while not q.empty():
        current = q.get()
        if current[1] == goal:
            return path[goal]
        for nn in neighbors(current[1]):
            maybeCost = path[current[1]] + cost(nn)
            if nn not in path or maybeCost < path[nn]:
                path[nn] = maybeCost
                prio = maybeCost + hDist(nn)
                q.put((prio, nn))
    print("Failas")


    

for i in range(len(data)):
    for j in range(len(data[0])):
        positions[(j,i)] = int(data[i][j])

ans = findRoute((0,0))
print("PART1: Shortest route: {}".format(ans))
ans = findRoute((0,0), True)
print("PART2: Shortest route: {}".format(ans))
