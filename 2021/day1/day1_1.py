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

k = 0
p = 200000000000000000000000000000000000000
kasvoi = 0
for i in data :
    k = int(i)
    if k > p:
        kasvoi += 1
    p = int(i)

print("PART1: kasvoi yhteensä: " + str(kasvoi) + " kertaa")

# PART 2
k = 0
p = 200000000000000000000000000000000000000
kasvoi = 0
for i in range(len(data)-3):
    k = int(data[i]) + int(data[i+1]) + int(data[i+2])
    p = int(data[i+1]) + int(data[i+2]) + int(data[i+3])
    if k < p:
        kasvoi += 1

print("PART2: kasvoi yhteensä: " + str(kasvoi) + " kertaa")
print('done')
