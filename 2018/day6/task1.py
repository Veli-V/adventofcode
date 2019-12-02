import os
import sys
import string
from array import *

#f = open('input_test.txt', 'r')
f = open('input_task.txt', 'r')

width = 10
height = 10

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
      if distance < minDistance:
        minDistance = distance
        grid[y][x] = point[2]
      elif distance == minDistance:
        grid[y][x] = '.'
      distance = 0

print('########################')

#for y in grid:
#    for x in y:
#      print(x, end='')
#    print()

areaSizes = [[0, False] for y in range(len(points))]
print(areaSizes)

for y in grid:
    for x in y:
      if str(x).isdigit():
        areaSizes[int(x)][0] += 1

for x in range(height):
  if str(grid[0][x]).isdigit():
    areaSizes[int(grid[0][x])][1] = True
  if str(grid[x][0]).isdigit():
    areaSizes[int(grid[x][0])][1] = True
  if str(grid[x][height-1]).isdigit():
    areaSizes[int(grid[x][height-1])][1] = True
  if str(grid[height-1][x]).isdigit():
    areaSizes[int(grid[height-1][x])][1] = True

maxArea = 0

for x in areaSizes:
  if x[0] > maxArea and x[1] == False:
    maxArea = x[0]

print("maksimi alue: " + str(maxArea))

print(areaSizes)

