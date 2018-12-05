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
minLength = sys.maxsize
minLetter = 'a'
charList = []

for x in line:
    charList.append(ord(x))

charListTMP = charList
#print(charList)
for x in range (65,91):
    #print(str(x) + ' ja ' + str(x+32) + ' eli ' + chr(x) + ' ja ' + chr(x+32))
    charListTMP = list(filter((x).__ne__, charListTMP))
    charListTMP = list(filter((x+32).__ne__, charListTMP))
    end = len(charListTMP)-1
    while i < end:
        #print('i= ' + str(i) + ' end=' + str(end))
        #print(str(charList[i]) + '-' + str(charList[i+1]))
        if abs(charListTMP[i] - charListTMP[i+1]) == 32:
            #print('täsmää')
            del charListTMP[i]
            del charListTMP[i]
            i -= 2
            end -= 2
            #print(end)
            #print(charListTMP)
        i += 1
    #print('lopullinen pituus kirjaimella ' + chr(x) + ' = ' + str(len(charListTMP)))
    if len(charListTMP) < minLength:
        minLength = len(charListTMP)
        minLetter = chr(x)
    charListTMP = charList
    i = 0

#print('lopullinen pituus = ' + str(len(charList)))
print('minimi pituus tuli kirjaimella: ' + str(minLetter) + ' saavuttaen pituuden: ' + str(minLength))