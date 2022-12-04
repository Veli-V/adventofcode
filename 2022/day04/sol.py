#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

#PART 1
overlappers = 0
for d in data:
    d = d.split(",")
    first = d[0].split("-")
    second = d[1].split("-")

    if int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
        #print("first0 {}, second0 {}, first1 {}, second1 {}".format(first[0], second[0], first[1], second[1]))
        overlappers += 1
        #print("1over: {} in {}".format(first, second))

    elif int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1]):
        overlappers += 1
        #print("2over: {} in {}".format(second, first))

print("Part 1:")
print("There was {} overlapping pairs".format(overlappers))

#part 2

overlappers = 0
for d in data:
    d = d.split(",")
    first = d[0].split("-")
    second = d[1].split("-")
    f1, f2 = int(first[0]), int(first[1])
    s1, s2 = int(second[0]), int(second[1])

    if f1 >= s1 and f1 <= s2:
        overlappers += 1
    elif f2 >= s1 and f2 <= s2:
        overlappers += 1
    elif s1 >= f1 and s1 <= f1:
        overlappers +=1
    elif s2 >= f1 and s2 <= f2:
        overlappers +=1


print("Part 2:")
print("There was {} overlapping pairs".format(overlappers))
