#!/usr/bin/env python3
import sys

#input_file = 'test_input.txt'
input_file = 'input.txt'


#with open(input_file) as f:
    #data = f.readlines()

data = []
folds = []
maxy, maxx = 0,0


file = open(input_file, "r")
for line in file:
    if line.strip() == '':
        continue
    if "fold" in line:
        folds.append(line.strip())
    else:
        data.append(line.strip())

     



dots = {}
for d in data:
    tmp = d.split(",")
    dots[int(tmp[0]),int(tmp[1])] = "#"
    maxx = max(int(tmp[0]), maxx)
    maxy = max(int(tmp[1]), maxy)


foldCount = 0
for f in folds:
    foldCount += 1
    foldDir = f.split(" ")[2]
    fold = int(foldDir.split("=")[1])
    foldDir = foldDir.split("=")[0]

    if foldDir == "y":
        for i in range(fold+1, maxy +1):
            for j in range(maxx+1):
                if (j,i) in dots.keys():
                    dots[(j,fold+(fold-i))] = "#"
                    del dots[(j,i)]
        maxy = fold -1
    elif foldDir == "x":
        for i in range(maxy +1):
            for j in range(fold, maxx+1):
                if (j,i) in dots.keys():
                    dots[(fold+(fold-j),i)] = "#"
                    del dots[(j,i)]
        maxx = fold -1
    if foldCount == 1:
        print("PART1: dots remaining after one fold: {}".format(len(dots)))

for i in range(maxy +1):
    for j in range(maxx + 1):
        print(dots.get((j,i), "."), end="")
    print()
