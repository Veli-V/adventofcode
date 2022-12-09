#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

visited = {}
visited2 = {}
directions = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0],
    "UL": [-1, 1],
    "UR": [1, 1],
    "DL": [-1, -1],
    "DR": [-1, 1]
}


h = [0, 0]
t = [0, 0]
t2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
s = [0, 0]

def printGame():
    if input_file != 'input.txt': size = 6
    else: return
    for i in range(size-1, -1, -1):
        for j in range(size):
            if [j, i] == s: print("S", end="")
            elif [j, i] == t: print("T", end="")
            elif [j, i] == h: print("H", end="")
            else: print(".", end="")
        print()
    print()

def addCoord(s, n):
    ans = [int(s[0]) + int(n[0]), int(s[1]) + int(n[1])]
    return ans

def checkDistance(tail, head):
    ans = [int(head[0]) - int(tail[0]), int(head[1]) - int(tail[1])]
    if abs(ans[0]) > 1 or abs(ans[1]) > 1:
        if ans[0] != 0:
            ans[0] = ans[0] / abs(ans[0])
        if ans[1] != 0:
            ans[1] = ans[1] / abs(ans[1])
    else:
        if ans[0] > 1:
            ans[0] = 1
        elif ans[0] < -1:
            ans[0] = -1
        else:
            ans[0] = 0
        if ans[1] > 1:
            ans[1] = 1
        elif ans[1] < -1:
            ans[1] = -1
        else:
            ans[1] = 0

    #print("H:{} , T:{} , ans: {}".format(h, t, ans))
    return ans

printGame()

for d in data:
    d = d.split(" ")
    for i in range(int(d[1])):
        h = addCoord(h, directions[d[0]])
        thMove = checkDistance(t, h)
        t = addCoord(t, thMove)
        t2[0] = t
        visited[str(t)] = 1
        for j in range(1, len(t2)):
            thMove = checkDistance(t2[j], t2[j-1])
            t2[j] = addCoord(t2[j], thMove)
        visited2[str(t2[8])] = 1

        #print(h)
        printGame()

print("PART1")
print("Tail visited {} squares".format(len(visited)))
print("PART2")
print("Tail9 visited {} squares".format(len(visited2)))
