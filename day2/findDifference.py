import os
import sys
import string

#f = open('input_test2.txt', 'r')
f = open('input_task.txt', 'r')

diff = 0
sama1 = ""
sama2 = ""

previousLines = []
for line in f:
    line = line.rstrip('\n')
    #print('nyt ' + line)
    for prev in previousLines:
        #print('verrataan: ' + line + " ja " + prev)
        for x in range(len(line)):
            if prev[x] != line[x]:
                diff += 1
            if diff > 1:
                diff = 0
                break
        if diff == 1:
            print('löydettiin close enought: ' + line + ' ja ' + prev)
            sama1 = line
            sama2 = prev
            break
    previousLines.append(line)
print(sama1 + '  '+ sama2)

for x in range(len(sama1)):
    if sama1[x] != sama2[x]:
        sama3 = sama1[0:x] + sama1[x+1:len(sama1)]
        print(sama1[0:x])
        print(sama1[x+1:len(sama1)])

print('yhteinen osa: ' + sama3)


