import os
import sys
import string
from array import *

#f = open('input_test.txt', 'r')
f = open('input_task.txt', 'r')

#width = 10
#height = 10

width = 365
height = 365

grid = [[0 for x in range(width)] for y in range(height)]
points = []
#print(grid)
pointName = 0
for line in f:
  splitted = line.split(',')
  grid[int(splitted[1])][int(splitted[0])] = pointName
  points.append([int(splitted[1]),int(splitted[0]), pointName])
  pointName += 1
#print(points)

distance = 0
minDistance = height

#for y in grid:
#    for x in y:
#      print(x, end='')
#    print()

string = ''
distanceSum = 0

for y in range(height):
  for x in range(width):
    string = str(grid[y][x])
    distance = 0
    minDistance = height
    #if not string.isdigit():
      #print('nada: ' + str(grid[y][x]))
      #continue
    for point in points:
      distance = abs(abs(y-point[0]) + abs(x-point[1]))
      #print(str(x) + ',' + str(y) + ' Etäisyys pisteestä: ' + str(point) + ' = ' + str(y) + '-' + str(point[0]) + '+' +  str(x) + '-' + str(point[1]) + '=' + str(distance))
      #if distance < minDistance:
      #  minDistance = distance
      #  grid[y][x] = point[2]
      #elif distance == minDistance:
      #  grid[y][x] = '.'
      distanceSum += distance
      distance = 0
    #print(distanceSum)
    if distanceSum < 10000:
      grid[y][x]= '#'
    distanceSum = 0

print('########################')

#for y in grid:
#    for x in y:
#      print(x, end='')
#    print()

areaSizes = [[0, False] for y in range(len(points))]
print(areaSizes)

areaSize = 0

for y in grid:
    for x in y:
      if str(x) == '#':
        areaSize += 1


print("alue on yhteensä: " + str(areaSize))

