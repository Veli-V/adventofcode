import os
import sys
import string
from array import *
from datetime import datetime

#f = open('input_test.txt', 'r')
f = open('input_task.txt', 'r')

width = 60
height = 6000
sleepingMinutes = [[0 for x in range(width)] for y in range(height)]

infos = []

# Change lines to tuples and store to array for sorting
for line in f:
  line = line.rstrip('\n')
  line = line.replace('[','')
  splitted = line.split(']')
  stringTime = splitted[0]
  stringTask = splitted[1]
  datetimeTime = datetime.strptime(stringTime, '%Y-%m-%d %H:%M')
  lineTuple = (datetimeTime, stringTask)
  infos.append(lineTuple)
  #print(datetimeTime.minute)

# sort the info we have
infosSorted = sorted(infos, key=lambda time: time[0])
#print(infos)
#print(infosSorted)

sleeping = False

for dataPoint in infosSorted:
  splitted = dataPoint[1].split(' ')
  #print(splitted)
  if splitted[1] == 'Guard':
    #print('Vartija vaihtui, vuorossa: ' + splitted[2])
    guard = splitted[2].replace('#','')
  if splitted[1] == 'falls':
    sleeping = True
    sleepingTimeStart = dataPoint[0]
    #print('vartija ' + guard + ' nukahti hetkellä ' + str(sleepingTimeStart))
  if splitted[1] == 'wakes':
    sleeping = False
    sleepingTimeStop = dataPoint[0]
    sleepingTime = sleepingTimeStop - sleepingTimeStart
    #print('vartija ' + guard + ' heräsi hetkellä ' + str(sleepingTimeStop) + ' nukkuen ' + str(sleepingTime))
    for x in range(sleepingTimeStart.minute, sleepingTimeStop.minute):
      sleepingMinutes[int(guard)][x] += 1

maxVartija = 0
maxMinuutti = 0
maxMinuutit = 0
maxKertoja = 0 
vartija = 0
kertoja = 0

for x in sleepingMinutes:
  summa = sum(x)
  minuutti = x.index(max(x))
  kertoja = max(x)
  #print(x)
  #print('vartija ' + str(vartija) +' yhteensä ' + str(summa) + ' nukkui eniten minuutilla ' + str(minuutti) + ' kertoja ' + str(kertoja) + ' nyt maxkertoja on ' + str(maxKertoja))
  if maxKertoja < kertoja:
    maxVartija = vartija
    maxMinuutti = minuutti
    maxKertoja = kertoja
  vartija += 1

print('Eniten nukkui vartija #' + str(maxVartija) + ' nukkuen enite minuutilla ' + str(maxMinuutti) + ' yhteensä ' + str(maxKertoja) + ' kertaa.')
print('Vastaus on siis ' + str(maxVartija*maxMinuutti))