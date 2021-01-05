#!/usr/bin/env python3

import sys
import ast
import re

#input_file = "test.txt"
#input_file = "test2.txt"
input_file = "input.txt"


with open(input_file) as f:
    data = f.read()

kws = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkInput(input):
    if int(input["byr"]) > 2002:
        #print("invalid byr")
        return False
    if int(input["byr"]) < 1920:
        #print("invalid byr")
        return False
    if int(input["iyr"]) < 2010:
        #print("invalid iyr")
        return False
    if int(input["iyr"]) > 2020:
        #print("invalid iyr")
        return False
    if int(input["eyr"]) > 2030:
        #print("invalid eyr")
        return False
    if int(input["eyr"]) < 2020:
        #print("invalid eyr")
        return False
    if input["hgt"][-2:] == "cm":
        if int(input["hgt"][:-2]) < 150:
            #print("invalid hgt")
            return False
        if int(input["hgt"][:-2]) > 193:
            #print("invalid hgt")
            return False
    elif input["hgt"][-2:] == "in":
        if int(input["hgt"][:-2]) < 59:
            #print("invalid hgt")
            return False
        if int(input["hgt"][:-2]) > 76:
            #print("invalid hgt")
            return False
    else:
        #print("invalid hgt")
        return False
    if re.match(r"(#\w{6}$)", input["hcl"]) is None:
        #print("HCL kusee")
        return False
    if input["ecl"] not in ecls:
        #print("ecl kusee")
        return False
    if re.match(r"\d{9}$", input["pid"]) is None:
        #print("Pid kusee")
        return False
    return True

okCount = 0

data = data.split("\n\n")
#print(len(data))
for d in data:
    dd = d.replace(" ", " , ")
    dd = dd.replace(":", " : ")
    ds = set(dd.split()) & set(kws)
    #print(dd)
    #print(ds)
    if len(ds) == 8:
        #print("Is okay, all in")
        okCount += 1
    if len(ds) == 7:
        if ("cid") not in ds:
            #print("Is okay, only cid is missing")
            okCount += 1


print("PART1: a'ok passports {}".format(okCount))

## PART 2

okCount = 0
for d in data:
    if len(d) > 0:
        dd = d.replace(" ", ", ")
        dd = dd.replace(":", " : ")
        dd = dd.replace("\n", " , ")
        dd = dd.strip(",")
        #print(dd)
        di = dict((x.strip(), y.strip())
                  for x,y in (element.split(':') for
                              element in dd.split(',')))
        #print(di)
        ds = set(dd.split()) & set(kws)
        #print(dd)
        #print(ds)
        if len(ds) == 8:
            validated = checkInput(di)
            if validated:
                #print("Is all ok")
                okCount += 1
        if len(ds) == 7:
            if ("cid") not in ds:
                validated = checkInput(di)
                if validated:
                    #print("Is all ok")
                    okCount += 1

print("PART2: a'ok passports {}".format(okCount))
