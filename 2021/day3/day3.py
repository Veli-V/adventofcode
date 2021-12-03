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

def oxygen(ar, r):
    tar = []
    ones = 0
    for d in ar:
        ones += int(d[r])

    if ones >= len(ar)/2:
        bit = 1
    else:
        bit = 0

    for d in ar:
        if d[r] == str(bit):
            tar.append(d)

    if len(tar) == 1:
        return (str(int(tar[0], 2)))

    else:
        return oxygen(tar, r+1)


def co2(ar, r):
    tar = []
    ones = 0
    for d in ar:
        ones += int(d[r])

    if ones < len(ar)/2:
        bit = 1
    else:
        bit = 0

    for d in ar:
        if d[r] == str(bit):
            tar.append(d)

    if len(tar) == 1:
        return (str(int(tar[0], 2)))
    else:
        return co2(tar, r+1)


if input_file == 'test_input.txt':
    gamma = [0,0,0,0,0]
else:
    gamma = [0,0,0,0,0,0,0,0,0,0,0,0]



for d in data:
    dicti[d] = 1
    for i in range(len(d)):
        gamma[i] += int(d[i])


gammastr = ''
epsilonstr = ''
for i in range(len(gamma)):
    if gamma[i] < len(data)/2:
        gammastr += '0'
        epsilonstr += '1'
    else:
        gammastr += '1'
        epsilonstr += '0'
tmp = ''

print("Gamma: " + gammastr + " ja epsilon: " + epsilonstr)
print("eli " + str(int(gammastr, 2)) + " ja " + str(int(epsilonstr, 2)))
print("PART1: " + (str(int(gammastr, 2) * int(epsilonstr, 2))))

# PART 2

ox = oxygen(data, 0)
co = co2(data, 0)
answer = int(ox) * int(co)

print("ox " + str(ox) + " co " + str(co))
print("PART2: " + str(answer))
