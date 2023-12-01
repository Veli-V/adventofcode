#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

numbers  = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbersl = ["o", "e", "o", "e", "r", "e", "x", "n", "t", "e"]
numbersf = ["z", "o", "t", "t", "f", "f", "s", "s", "e", "n"]
#print(data)
tmpl = ""
ans = 0


#part1
for d in data:
    tmpl = ""
    for c in d:
        if c.isdigit():
            tmpl += c
            break
    for c in reversed(d):
        if c.isdigit():
            tmpl += c
            break
    ans += int(tmpl)

print("Part 1:")
print(ans)

ans = 0
# part2
for d in data:
    tmpl = ""
    for idc, c in enumerate(d):
        if c.isdigit():
            tmpl += c
            break
        if c in numbersf:
            for n in numbers:
                if d[int(idc):int(idc)+len(n)] in numbers:
                    #print(d[int(idc):int(idc)+len(n)])
                    tmpl += str(numbers.index(d[int(idc):int(idc)+len(n)]))
                    #print(tmpl)
                    break
        if len(tmpl) > 0:
            break
    for idc, c in enumerate(reversed(d)):
        #print(idc, c)
        if c.isdigit():
            tmpl += c
            break
        if c in numbersl:
            #print("c in numbersl")
            for n in numbers:
                tmps = d[len(d)-len(n)-idc:len(d)-idc]
                #print(tmps)
                if tmps in numbers:
                    tmpl += str(numbers.index(tmps))
                    break
                tmps = ""
        if len(tmpl) > 1:
            break

    #print(tmpl)
    ans += int(tmpl)

print("Part 2:")
print(ans)

