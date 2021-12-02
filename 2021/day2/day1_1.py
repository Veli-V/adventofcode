#!/usr/bin/env python3
import sys

#input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
# PART one

commands = dict(forward = [1,0], down = [0,1], up = [0,-1])
print(commands)

position =  [0,0]
for d in data:
    d = d.split()
    position[0] += commands[d[0]][0] * int(d[1])
    position[1] += commands[d[0]][1] * int(d[1])

print(position)
print("PART1: Answer: " + str(position[0] * position[1]))

# PART 2
position =  [0,0]
aim = 0
for d in data:
    d = d.split()
    aim += commands[d[0]][1] * int(d[1])
    position[0] += commands[d[0]][0] * int(d[1])
    position[1] += commands[d[0]][0] * int(d[1]) * aim

print(position)
print("PART2: Answer: " + str(position[0] * position[1]))
