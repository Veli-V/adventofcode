import os
import sys
import string
from array import *

f = open('input_test.txt', 'r')
#f = open('input_task.txt', 'r')

height = 6   # For Test 6, for task 26
width = 1
ABCCONSTANT = 65

completedSteps = []

orderArray = [[0 for x in range(width)] for y in range(height)]
abcList = list(string.ascii_uppercase)

def canBeDone(x):
  if len(x[1]) == 0:
    return True
  return False

def completeStep(step):
  if step == 'Done':
    #print("ollaan tehty jo")
    return
      
  #print('koitetaan tehdä: ' + step)
  i = 0
  stepInt = ord(step)-ABCCONSTANT
  end = len(orderArray[stepInt][1])
  while i < end:
    #print(step + ' Tarvii ainakin: ' + orderArray[stepInt][1][i])
    completeStep(orderArray[stepInt][1][i])
    end -= 1
    i += 1

  #print("tehtiin nyt sit: " + step)
  for x in orderArray:
    try:
      x[1].remove(step)
    except ValueError:
      pass
    #print("poiston jälkee: ", end='')
    #print(x)
  orderArray[stepInt][0] = 'Done'
  completedSteps.append(step[0])



for x in range(height):
  orderArray[x][0] = abcList[x]
  orderArray[x].append([])
  #orderArray[x].append(ord(abcList[x])-ABCCONSTANT +1)

#for y in orderArray:
  #print(y)

for line in f:
  line = line.rstrip('\n')
  splitted = line.split(' ')
  #print("valmiina pitää olla " + splitted[1] + ' ennen ' + splitted[7])
  orderArray[ord(splitted[7])-ABCCONSTANT][1].append(splitted[1])

for y in orderArray:
  print(y)

for y in orderArray:
  #print(y)
  completeStep(y[0])
  

print('Taskit suoritettiin järjestyksessä: ', end = '') 
for y in completedSteps:
  print(y, end='')
print()