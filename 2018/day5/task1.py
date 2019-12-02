import os
import sys
import string
from array import *

#f = open('input_test.txt', 'r')
f = open('input_task.txt', 'r')

line = f.readline()
f.close()
#print(line)
end = len(line)-1
i = 0

charList = []

for x in line:
    charList.append(ord(x))
#print(charList)
while i < end:
    #print(str(charList[i]) + '-' + str(charList[i+1]))
    if abs(charList[i] - charList[i+1]) == 32:
        #print('täsmää')
        del charList[i]
        del charList[i]
        i -= 2
        end -= 2
        #print(charList)
    i += 1

print('lopullinen pituus = ' + str(len(charList)))