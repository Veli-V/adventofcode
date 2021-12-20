#!/usr/bin/env python3

import sys
import queue
import numpy as np

input_file = 'input.txt'

with open(input_file) as f:
    data = f.readline()



#data = "D2FE28"
#
#dataEsimerkit = [ \
#                  "D2FE28"    , \
#                  "38006F45291200", \
#                  "EE00D40C823060", \
#                  "8A004A801A8002F478", \
#                  "620080001611562C8802118E34", \
#                  "C0015000016115A2E0802F182340", \
#                  "A0016C880162017C3686B18A3D4780"]
#binEsimerkit = [ \
#                 "110100101111111000101000", \
#                 "00111000000000000110111101000101001010010001001000000000", \
#                 "11101110000000001101010000001100100000100011000001100000"]
#
#
#
#data = dataEsimerkit[0]
data = data.strip()
data = bin(int(data, 16))[2:].ljust(4*len(data), '0')
#data = bin(int(data, 16))[2:].zfill(4*len(data))
#data = bin(int(data, 16))[2:]

def type4(d):
    val = ''
    while d[0] == "1":
        val += d[1:5]
        d = d[5:]
    val += d[1:5]
    d = d[5:]
    return int(val, 2), d

def parse(d):
    d = d.strip()
    value = 0
    version, typeID, d = int(d[:3], 2), int(d[3:6], 2), d[6:]
    if typeID == 4:
        value, d = type4(d)
    else:
        subValues = []
        lenId, d = int(d[0]), d[1:]
        if lenId == 0:
            length, d = int(d[:15], 2), d[15:]
            subd, d = d[:length], d[length:]
            while subd != "":
                subver, subval, subd = parse(subd)
                subValues.append(subval)
                version += subver
        else:
            packCount, d = int(d[:11],2), d[11:]
            for i in range(packCount):
                subver, subval, d = parse(d)
                subValues.append(subval)
                version += subver
        if typeID == 0:
            value = sum(subValues)
        elif typeID == 1:
            value = np.prod(subValues)
        elif typeID == 2:
            value = min(subValues)
        elif typeID == 3:
            value = max(subValues)
        elif typeID == 5:
            value = 1 if subValues[0] > subValues[1] else 0
        elif typeID == 6:
            value = 1 if subValues[0] < subValues[1] else 0
        elif typeID == 7:
            value = 1 if subValues[0] == subValues[1] else 0


    return version, value, d

i = 0
version = -1
type = -1
packets = 0
ans = 0

version, value, packet = parse(data)
print("PART1: {}".format(version))
print("PART2: {}".format(value))

