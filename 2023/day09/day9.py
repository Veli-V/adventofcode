#!/usr/bin/env python3
import sys

input_file = "test.txt"
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
data = [d.split() for d in data]
#print(data)

def findSequency(seq):
    #print("tutkitaan: ", seq)
    i = 1
    b, e = 0, 0
    tmpS = []
    while i < len(seq):
        tmpS.append(seq[i] - seq[i-1])
        i += 1

    if all(t == 0 for t in tmpS):
        #print("Palautetaan: ", seq[-1])
        return seq[-i], seq[0]
    e, b = findSequency(tmpS)
    #print("palautetaan: ", seq[-1] + i)
    return seq[-1] + e, seq[0] - b


ans, tmp, ans2, tmp2 = 0, 0, 0, 0
for d in data:
    d = [int(dd) for dd in d]
    tmp, tmp2 = findSequency(d)
    #print("e: ", tmp, "b: ", tmp2)
    ans += tmp
    ans2 += tmp2

print("part1: ", ans)
print("part2: ", ans2)
