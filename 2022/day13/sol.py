#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
#input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

data.clear()
with open(input_file) as f:
    line = f.readline().strip()
    while line:
        data.append(line)
        line = f.readline().strip()
        data.append(line)
        line = f.readline().strip()
        line = f.readline().strip()



print(data)

for i in range(1, len(data), 2):
   left = data[i-1]
   right = data[i]
   print("comparing {} and {}".format(left, right))
