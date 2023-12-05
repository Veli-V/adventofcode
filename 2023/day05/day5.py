#!/usr/bin/env python3
import sys

input_file = "test.txt"
#input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

seeds = []
sts, stf, ftw, wtl, ltt, tth, htl = [], [], [], [], [], [], []
state = "seed"

with open(input_file) as f:
    seeds = f.readline().split(":")[1].split()
    #data = f.readlines()
    for line in f:
        line = line.strip()
        #print(state, line)
        #print(line)
        if len(line) > 0:
                if line ==  "seed-to-soil map:":
                    state = "sts"
                elif line == "soil-to-fertilizer map:":
                    state = "stf"
                elif line == "fertilizer-to-water map:":
                    state = "ftw"
                elif line == "water-to-light map:":
                    state = "wtl"
                elif line == "light-to-temperature map:":
                    state = "ltt"
                elif line == "temperature-to-humidity map:":
                    state = "tth"
                elif line == "humidity-to-location map:":
                    state = "htl"
                elif state == "sts":
                    sts.append([int(i) for i in line.split()])
                elif state == "stf":
                    stf.append([int(i) for i in line.split()])
                elif state == "ftw":
                    ftw.append([int(i) for i in line.split()])
                elif state == "wtl":
                    wtl.append([int(i) for i in line.split()])
                elif state == "ltt":
                    ltt.append([int(i) for i in line.split()])
                elif state == "tth":
                    tth.append([int(i) for i in line.split()])
                elif state == "htl":
                    htl.append([int(i) for i in line.split()])

#data = [d.strip() for d in data]
seeds = [int(i) for i in seeds]
print("Seeds: ", seeds)
print("sts: ", sts)
print("stf: ", stf)
print("ftw: ", ftw)
print("wtl: ", wtl)
print("ltt: ", ltt)
print("tth: ", tth)
print("htl: ", htl)
