#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
# PART one


pointsDict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

points = 0
for d in data:
    points += pointsDict[d]

print("PART1: ")
print(points)

# x = häviö
# y = tasuri
# z = voitto

templist = ['C', 'A', 'B', 'C', 'A']
valueDict = {
    'A': 1,
    'B': 2,
    'C': 3
}
toDoDict = {
    'X': -1,
    'Y': 0,
    'Z': 1
}
resultPointDict = {
    'X': 0,
    'Y': 3,
    'Z': 6

}

points = 0
rndPoints = 0
whatToDo = 'A'
index = 0
for d in data:
    index = valueDict[d[0]] + toDoDict[d[2]]
    whatToDo = templist[index]
    rndPoints = resultPointDict[d[2]] + valueDict[whatToDo]
    points += rndPoints

print("Part2: ")
print(points)
