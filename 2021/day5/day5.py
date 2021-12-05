#!/usr/bin/env python3
import sys

#input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

pipes = {}
for d in data:
    x1 = int(d.split("->")[0].split(",")[0].strip())
    y1 = int(d.split("->")[0].split(",")[1].strip())
    x2 = int(d.split("->")[1].split(",")[0].strip())
    y2 = int(d.split("->")[1].split(",")[1].strip())

    if (x1 == x2):
        for i in range(min(y1,y2), max(y1,y2)+1):
            index = (str(x1) + "," + str(i))
            if index in pipes:
                pipes[index] += 1
            else:
                pipes[index] = 1

    elif (y1 == y2):
        for i in range(min(x1,x2), max(x1,x2)+1):
            index = (str(i) + "," + str(y1))
            if index in pipes:
                pipes[index] += 1
            else:
                pipes[index] = 1
    else:
        for i in range(max(x1,x2) - min(x1,x2)+1):
            if (y1 > y2):
                y = y1-i
            else:
                y = y1+i
            if (x1 > x2):
                x = x1-i
            else:
                x = x1+i
            index = (str(x) + "," + str(y))
            if index in pipes:
                pipes[index] += 1
            else:
                pipes[index] = 1

            



print()
for y in range(10):
    for x in range(10):
        index = str(x) + "," + str(y)
        if index in pipes:
            print(pipes[index], end="")
        else:
            print(".", end="")
    print()

print()
answer = 0
for v in pipes.values():
    if v > 1:
        answer += 1

print("PART1:" + str(answer))
