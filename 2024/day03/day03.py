#!/usr/bin/env python3
import sys
import re

input_file = 'input.txt'
#input_file = 'test.txt'
#input_file = 'test2.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.read().rstrip()


#Part1
multis = re.findall("mul\([0-9]*,[0-9]*\)", data)
ans = 0

for m in multis:
    d = m[4:-1].split(",")
    #print(d)
    ans += int(d[0]) * int(d[1])

print("Part1: ", ans)

#Part2

ans = 0
numbers = []
i = 0
j = 0
tmp = []
tmpst = ""
do = True

pattern = re.compile("[0-9]*,[0-9]*")
while i < len(data):
    d = data[i]
    match d:
        case 'm':
            if data[i:i+4] == "mul(":
                j = data.find(')', i+4)
                if j != -1:
                    tmpst = data[i+4:j]
                    #print(tmpst)
                    if pattern.fullmatch(tmpst) and do:
                        tmp = tmpst.split(",")
                        ans += int(tmp[0]) * int(tmp[1])
                        #print("ok")
                        i = j
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1
        case 'd':
            #print(data[i:i+4], data[i:i+7])
            if data[i:i+4] == "do()":
                #print("do")
                do = True
                i += 4
            elif data[i:i+7] == "don't()":
                #print("Don't")
                do = False
                i += 7
            else:
                i += 1
        case _:
            i+=1


print("Part2: ", ans)
