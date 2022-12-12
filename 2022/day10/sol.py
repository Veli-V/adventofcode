#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = 'test2.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
#print(data)

cycle, toAdd, strenght = 0, 0, 0
x = 1
read = True
cont = True
print()
print("Part2:")
while(cont):
    #print("cycle:           {}".format(cycle))
    #print("Drawing position {}".format(cycle%40))
    #print("sprite pos:      {}".format(x))
    #part2:
    if cycle % 40 == 0:
        print()
    if cycle % 40 in range(x-1, x+2):
        print("#", end="")
    else:
        print(".", end="")


    cycle += 1
    #part1:
    if cycle == 20 or (cycle -20) % 40 == 0:
        #print("At cycle:{}, value = {}, signal strenght={}".format(cycle, x, x*cycle))
        strenght += x*cycle
    if read:
        d = data.pop(0).split(" ")
        if (d[0] == "addx"):
            read = False
            toAdd = int(d[1])
    else:
        x += toAdd
        read = True

    if read and not data:
        cont = False

print()
print("PART1:")
print("Sum of signal strenghts: {}".format(strenght))
