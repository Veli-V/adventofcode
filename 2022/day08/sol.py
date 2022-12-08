#!/usr/bin/env python3
import sys

#input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

forest = []
tmpl = []

for d in data:
    for c in d:
        tmpl.append(int(c))
    forest.append(tmpl.copy())
    tmpl.clear()

print("    ", end = "")
for i in range(len(forest[0])):
    print(i % 10, end=" ")
print()
print()
c = 0
for f in forest:
    print(str(c).zfill(2), end ="  ")
    c += 1
    print(*f)
print()

#for i in range(2,5):
    #print(i)
coords = "0,0"
seens = 0
scenicMax = 0
for i in range(1, len(forest)-1):
    #print(* forest[i])
    for j in range(1, len(forest[0])-1):
        #print(forest[i][j], end=" ")
        tree = int(forest[i][j])
        seen = False
        sseen = False
        uMax = 0
        bMax = 0
        counter = 0
        scenic = 1
        # up
        for k in range(i-1, -1, -1):
            counter += 1
            if forest[k][j] >= tree and not sseen:
                scenic *= counter
                sseen = True
            if uMax < int(forest[k][j]): uMax = int(forest[k][j])
        if not sseen:
            scenic *= i
        counter = 0
        sseen = False
        # down
        for k in range(i+1, len(forest)):
            counter += 1
            if forest[k][j] >= tree and not sseen:
                scenic *= counter
                sseen = True
            if bMax < int(forest[k][j]): bMax = int(forest[k][j])
        if not sseen:
            scenic *= len(forest)-i-1
        counter = 0
        sseen = False
        # left
        for k in range(j-1, -1, -1):
            counter += 1
            if forest[i][k] >= tree and not sseen:
                scenic *= counter
                sseen = True
        if not sseen:
            scenic *= j
        counter = 0
        sseen = False
        # right
        for k in range(j+1, len(forest[i])):
            counter += 1
            if forest[i][k] >= tree and not sseen:
                scenic *= counter
                sseen = True
        if not sseen:
            scenic *= len(forest[i])-j-1


        if max(forest[i][:j]) < tree: seen = True
            #print("näkyy vasemmalta")
        elif max(forest[i][j+1:]) < tree: seen = True
            #print("näkyy oikealta")
        elif uMax < tree: seen = True
            #print("tmpMax: {}, tree {}".format(tmpMax, tree))
            #print("näkyy ylhäältä")
        elif bMax < tree: seen = True
            #print("tmpMax: {}, tree {}".format(tmpMax, tree))
            #print("näkyy alhaalta")
        if seen:
            seens += 1
        if scenic > scenicMax:
            scenicMax = scenic
            coords = str(i) + ":" + str(j)

        #:print("Coords: {}:{} Tree: {}, scenic {}, scenimax {}".format(i, j, tree, scenic, scenicMax))

#sides:
seens += len(forest)*2
seens += len(forest[0])*2
seens -= 4
print("Part1:")
print("I have seen: {} trees".format(seens))

#Part2
print("Part2:")
print("at coords: {}".format(coords))
print("Highest scenic score {}".format(scenicMax))
