#!/usr/bin/env python3
import sys
import math

#input_file = 'test_input.txt'
input_file = 'input.txt'


with open(input_file) as f:
    data = f.readlines()
data = [int(n) for n in data[0].split(",")]


# PART1
length = len(data)
mid = int((length-1)/2)

if (length % 2 == 0):
    median = [data[mid], data[mid+1]]
else:
    median = [data[mid]]

print(median)

min = 9000000000
fuel = 0
target = 0

for m in median:
    for d in data:
        fuel += abs(m - d)
    if fuel < min:
        min = fuel
        target = m
    fuel = 0

print("PART1: by moving to {} craps use only {} fuel".format(target, min))

#PART 2

mid = sum(data)/len(data)
median = [math.floor(mid), math.ceil(mid)]

min = 9000000000
fuel = 0
target = 0

for m in median:
    for d in data:
        fuel += sum(range(abs(m - d)+1))

    if fuel < min:
        min = fuel
        target = m
    fuel = 0

print("PART2: by moving to {} craps use only {} fuel".format(target, min))
