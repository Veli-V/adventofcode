#!/usr/bin/env python3

import sys
#from treelib import Node, Tree

#input_file = "test.txt"
#input_file = "test2.txt"
input_file = "input.txt"

# 5 for test.txt, 25 for input.txt
data = []
with open(input_file) as f:
    for l in f:
        data.append(int(l))


data.sort()
#print(data)

stepCount = [0,0,1]
prev = 0

for d in data:
    stepCount[d-prev-1] += 1
    prev = d

answer = stepCount[0] * stepCount[2]
print("PART1: 1 step differences times 3 step differences is {}".format(answer))

#part 2
#tmpi = 1
#tree = Tree()
#nameCounter = 2
#
#
#def addChilds(parent):
#    global nameCounter
#    index = data.index(parent.tag)
#    #print(index)
#    #print(data[index])
#    #print(data[index+1])
#    c = 1
#    while index +c < len(data) and data[index+c] - data[index] <= 3:
#        #print("kekkonen")
#        nameCounter += 1
#        tree.create_node(data[index+c], nameCounter, parent=parent)
#        addChilds(tree.get_node(nameCounter))
#        c += 1
#    return
#
#tree.create_node(0, 0)
#parent=tree.get_node(0)
#i = 0
#while data[i] <= 3:
#    nameCounter += 1
#    print(data[i])
#    tree.create_node(data[i], nameCounter, parent=parent)
#    print(tree.get_node(nameCounter))
#    addChilds(tree.get_node(nameCounter))
#    i += 1
##tree.show()
##addChilds(parent)
##tree.show()
#leaves = tree.leaves()
##print(leaves)
#answer = len(leaves)
#print("PART2: Different compilations are {}".format(answer))
#
#
##for i in range(len(data)):
#    #while data[tmpi] - data[i] <= 3:
#        #tree.create_node(data[tmpi], data[tmpi], parent=parent)
#        #tmpi += 1
#    #tmpi = i+2
#    #tree.show()


possibilities = {}
values = {}
tmpList = []
c = 1

for d in data:
    if d <= 3:
        tmpList.append(d)
    else:
        break

possibilities[0] = tmpList.copy()
tmpList.clear()

for i in range(len(data)):
    while i + c < len(data) and data[i+c] - data[i] <= 3:
        tmpList.append(data[i+c])
        c += 1
    c = 1
    possibilities[data[i]] = tmpList.copy()
    tmpList.clear()

#print(possibilities)

data.reverse()
for d in data:
    values[d] = 0

values[max(data)] = 1
values[0] = 0
for d in data:
    for p in possibilities[d]:
        values[d] += values[p]

for p in possibilities[0]:
    values[0] += values[p]
#print(values)


print("PART2: Answer is {}".format(values[0]))
