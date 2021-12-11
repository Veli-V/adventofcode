#!/usr/bin/env python3

# Disclaimer: I haven't made this ugly code for a while,
# but this was solved during cottage weekend with more than
# couple of beers
import sys
import queue

#input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = 'easymode'

with open(input_file) as f:
    data = f.readlines()

rounds = 1000000

octopi = {}
neughbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
flashed = []
ans = 0
print()

def printOctopi():
    for i in range(len(data)):
        for j in range(len(data[0])):
            if octopi[i,j] == 0:
                print("X", end="")
            else:
                print(octopi[i,j], end="")
        print()
    print()

def flash(oct):
    temp = (0,9)
    if octopi[oct] > 9:
        flashed.append(oct)
        for n in neughbors:
            temp = (oct[0]+n[0], oct[1]+n[1])
            if temp in octopi.keys() and temp not in flashed:
                octopi[temp] +=1
                flash(temp)


for i in range(len(data)):
    data[i] = data[i].strip()
    for j in range(len(data[0])):
        octopi[i,j] = int(data[i][j])

#printOctopi()
ans2 = 0
for x in range(rounds):
    # kasvatetaan numerot:
    for i in range(len(data)):
        for j in range(len(data[0])):
            octopi[i,j] += 1
    for i in range(len(data)):
        for j in range(len(data[0])):
            if octopi[i,j] > 9 and (i,j) not in flashed:
                flash((i,j))
    for i in range(len(data)):
        for j in range(len(data[0])):
            if octopi[i,j] > 9:
                octopi[i,j] = 0
    #printOctopi()
    if len(flashed) == 100:
        ans2 = x+1
        break
    if x < 100:
        ans += len(flashed)
    flashed.clear()




print("PART1: After 100 rounds, there has been {} flashes".format(ans))
print("PART2: All will flash at round {}".format(ans2))
print("done")
