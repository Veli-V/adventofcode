import os
import sys
import string
from array import *

width = 1000
height = 1000
fabric = [[0 for x in range(width)] for y in range(height)]

#for x in fabric:
#    for y in x:
#        print(y, end = " ")
#    print()
#print('XXXXXXXXXXXXXXXXXXXXXXXX')

#f = open('input_test.txt', 'r')
f = open('input_task.txt', 'r')

for line in f:
    line = line.rstrip('\n')
    #print(line)
    splitted = line.split('@')
    #print(splitted)
    splitted = splitted[1].split(':')
    #print(splitted)
    fromleft = int(splitted[0].split(',')[0])
    fromtop= int(splitted[0].split(',')[1])
    #print(str(fromleft) + ' ' + str(fromtop))
    width = int(splitted[1].split('x')[0])
    height = int(splitted[1].split('x')[1])
    #print(str(width) + ' ' + str(height))
    for y in range (fromtop, fromtop+height):
        #print('y: ' + str(y))
        for x in range (fromleft, fromleft+width):
            #print('x: ' + str(x))
 #           print(str(y) + ':' + str(x))
 #           print(fabric[y][x])
            fabric[y][x] += 1

    #print("kuole")

sum = 0
#for x in fabric:
#    for y in x:
#        print(y, end = " ")
#    print()
for y in range(len(fabric)):
    for x in range(len(fabric[y])):
        if fabric[y][x] > 1:
            sum += 1
print('päällekkäisiä: ' + str(sum)) 