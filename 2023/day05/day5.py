#!/usr/bin/env python3
import sys

input_file = "test.txt"
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

seeds = []
sts, stf, ftw, wtl, ltt, tth, htl = [], [], [], [], [], [], []

def checkInMap(seed, map):
    for m in map:
        if seed in range(m[1], m[1]+m[2]):
            return m[0] + seed - m[1]
    return seed

def checkInMapReverse(seed, map):
    for m in map:
        if seed > m[0] and seed < m[0]+m[2]+1:
            return m[1] + seed - m[0]
    return seed




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
print(seeds)
seeds = [int(i) for i in seeds]
# Check seeds loop

ans = sys.maxsize
for s in seeds:
    soil = checkInMap(s, sts)
    ferti = checkInMap(soil, stf )
    water = checkInMap(ferti, ftw )
    light = checkInMap(water, wtl )
    temp = checkInMap(light, ltt )
    humi = checkInMap(temp, tth )
    loc = checkInMap(humi, htl )
    if loc < ans:
        ans = loc
    #print(s, "->", soil, "->", ferti, "->", water, "->", light, "->", temp, "->", humi, "->", loc)

print("Part1: ", ans)

#part2
i = 0
seeds2 = []
while i < len(seeds):
    seeds2.append([seeds[i], seeds[i] + seeds[i+1]])
    i += 2

print(seeds2)

ans = sys.maxsize
i = 9975120
found = False
while i < sys.maxsize:
    if i%100000 == 0:
        print(i)
    humi = checkInMapReverse(i, htl)
    temp = checkInMapReverse(humi, tth)
    light = checkInMapReverse(temp, ltt)
    water = checkInMapReverse(light, wtl)
    ferti = checkInMapReverse(water, ftw)
    soil = checkInMapReverse(ferti, stf)
    seed = checkInMapReverse(soil, sts)
    for s in seeds2:
        if seed in range(s[0], s[1]+1):
            print("löytyi, siemen: ", seed, " paikka: ", i)
            found = True
            break
    if not found:
        i += 1
    else:
        break



print("Part2: ", i)
