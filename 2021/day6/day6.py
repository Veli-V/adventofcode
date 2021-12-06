#!/usr/bin/env python3
import sys

#input_file = 'test_input.txt'
#input_file = 'onefish.txt'
input_file = 'input.txt'

days = 256

#with open(input_file) as f:
#    data = f.readlines()
#data = [int(n) for n in data[0].split(",")]
#
## PART1
#for j in range(days):
#    for i in range(len(data)):
#        if data[i] == 0:
#            data.append(8)
#            data[i] = 6
#        else:
#            data[i] -= 1
#    #print("day: " + str(j+1) + " yhteensä: " + str(len(data)),end="")
#    #print(data)
#
#print("PART1: After " + str(days ) + " days: " + str(len(data)))

##Part 2

with open(input_file) as f:
    data = f.readlines()
data = [int(n) for n in data[0].split(",")]

fisuja = [0,0,0,0,0,0,0,0,0]

for d in data:
    fisuja[d] += 1


for i in range(days):
    tmp = fisuja[0]
    for j in range(6):
        fisuja[j] = fisuja[j+1]

    fisuja[6] = tmp + fisuja[7]
    fisuja[7] = fisuja[8]
    fisuja[8] = tmp

print("PART2:" + str(sum(fisuja)))
