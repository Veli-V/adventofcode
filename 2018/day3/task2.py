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
unique = True
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
f.close()
f = open('input_task.txt', 'r')
for line in f:
    unique = True
    line = line.rstrip('\n')
    splitted = line.split('@')
    id = splitted[0]
    splitted = splitted[1].split(':')

    fromleft = int(splitted[0].split(',')[0])
    fromtop= int(splitted[0].split(',')[1])
    width = int(splitted[1].split('x')[0])
    height = int(splitted[1].split('x')[1])
    for y in range (fromtop, fromtop+height):
        for x in range (fromleft, fromleft+width):
            if int(fabric[y][x]) > 1:
                unique = False
    if unique:
        print("uniikki on: " + id)
            



