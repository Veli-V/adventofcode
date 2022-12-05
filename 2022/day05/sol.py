#!/usr/bin/env python3
import sys
import queue

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
#print(data)

stacks = []

if input_file == 'test_input.txt':
    stacks.append(['Z', 'N'])
    stacks.append(['M', 'C', 'D'])
    stacks.append(['P'])
elif input_file == 'input.txt':
    stacks.append(['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'])
    stacks.append(['W', 'P', 'Q', 'G', 'S'])
    stacks.append(['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'])
    stacks.append(['F', 'Z', 'P', 'C', 'G', 'D', 'L'])
    stacks.append(['T', 'P', 'S'])
    stacks.append(['H', 'D', 'F', 'W', 'R', 'L'])
    stacks.append(['Z', 'N', 'D', 'C'])
    stacks.append(['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'])
    stacks.append(['R', 'M', 'S', 'G', 'Z', 'W', 'V'])



#PART 1

for d in data:
    command = d.split(' ')
    fromi = stacks[int(command[3])-1]
    to = stacks[int(command[5])-1]
    for i in range(int(command[1])):
        move = fromi.pop()
        to.append(move)

tops = ''

for s in stacks:
    tops += s.pop()

print("PART1")
print(tops)

#part2
stacks.clear()

if input_file == 'test_input.txt':
    stacks.append(['Z', 'N'])
    stacks.append(['M', 'C', 'D'])
    stacks.append(['P'])
elif input_file == 'input.txt':
    stacks.append(['D', 'M', 'S', 'Z', 'R', 'F', 'W', 'N'])
    stacks.append(['W', 'P', 'Q', 'G', 'S'])
    stacks.append(['W', 'R', 'V', 'Q', 'F', 'N', 'J', 'C'])
    stacks.append(['F', 'Z', 'P', 'C', 'G', 'D', 'L'])
    stacks.append(['T', 'P', 'S'])
    stacks.append(['H', 'D', 'F', 'W', 'R', 'L'])
    stacks.append(['Z', 'N', 'D', 'C'])
    stacks.append(['W', 'N', 'R', 'F', 'V', 'S', 'J', 'Q'])
    stacks.append(['R', 'M', 'S', 'G', 'Z', 'W', 'V'])

tmpstack = []
for d in data:
    command = d.split(' ')
    fromi = stacks[int(command[3])-1]
    to = stacks[int(command[5])-1]
    for i in range(int(command[1])):
        move = fromi.pop()
        tmpstack.append(move)
    for i in range(len(tmpstack)):
        to.append(tmpstack.pop())


tops = ''

for s in stacks:
    tops += s.pop()

print("PART2")
print(tops)
