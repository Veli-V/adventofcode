#!/usr/bin/env python3
import sys

input_file = "test.txt"
#input_file = "input.txt"


with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

#part 1
#print(data)
count = 0
pswok = False
okpsws = 0

for line in data:
    l = line.split(" ")
    #print(l)
    for c in l[2]:
        #print("verrataan {} ja {}".format(c, l[1][0]))
        if c == l[1][0]:
            count += 1
            #print("Mätsi! count nyt {}".format(count))
    rule = l[0].split("-")
    plow = int(rule[0])
    phigh = int(rule[1])
    if count <= phigh:
        if count >= plow:
            pswok = True
            okpsws += 1
    #print("salasana {} säännöllä {} osumia {} eli salasana ok {}".format(l[2], l[0], count, pswok))
    pswok = False
    count = 0

print("part1: ok salasanoja oli: {}".format(okpsws))

count = 0
pswok = False
okpsws = 0

for line in data:
    l = line.split(" ")
    rule = l[0].split("-")
    plow = int(rule[0])-1
    phigh = int(rule[1])-1
    #print(l)
    for c in l[2]:
        #print("verrataan {} ja {}".format(c, l[1][0]))
        if c == l[1][0]:
            count += 1
            #print("Mätsi! count nyt {}".format(count))
    if l[2][plow] == l[1][0]:
        count += 1
    if l[2][phigh] == l[1][0]:
        count += 1
    if count == 1:
        pswok = True
    print("salasana {} säännöllä {} osumia {} eli salasana ok {}".format(l[2], l[0], count, pswok))
    pswok = False
    count = 0

print("ok salasanoja oli: {}".format(okpsws))
