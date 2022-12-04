#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

var='a'
alphabets=[]
# starting from the ASCII value of 'a' and keep increasing the
# value by i.
alphabets=[(chr(ord(var)+i)) for i in range(26)]
var='A'
for i in range(26):
    alphabets.append(chr(ord(var)+i))

# PART one

sum = 0
for d in data:
   ind = int(len(d)/2)
   firstCom = d[:ind]
   secondCom = d[ind:]
   commonChar = set(firstCom).intersection(secondCom).pop()
   value = alphabets.index(commonChar) +1
   sum += value

print("PART1:")
print("Sum of priorities: {}".format(sum))

# PART two
i = 0
sum = 0
while i < len(data):
    elf1 = data[i]
    elf2 = data[i+1]
    elf3 = data[i+2]
    auth = set(elf1).intersection(elf2).intersection(elf3).pop()
    i += 3
    value = alphabets.index(auth) +1
    sum += value

print("PART2:")
print("Sum of priorities: {}".format(sum))
