import os
import sys
import string

#f = open('input_test.txt', 'r')
f = open('input_task.txt', 'r')
sumDouble = 0
sumTriple = 0
tuplia = False
triploja = False
abcArray = [-1]*26
abcList = list(string.ascii_lowercase)
print(abcArray)
for line in f:
    line = line.rstrip('\n')
    print(line)
    for a in abcList:
        abcArray[ord(a)-97] = 0
    for a in line:
        abcArray[ord(a)-97] += 1
    for a in abcArray:
        if a == 2:
            tuplia = True
        if a == 3:
            triploja = True
    if tuplia:
        sumDouble += 1
    if triploja:
        sumTriple += 1
    tuplia = False
    triploja = False
print('tuplia: ' + str(sumDouble) + ' triploja: ' + str(sumTriple) + ' ja niiden tulo: ' + str(sumDouble * sumTriple))
