#!/usr/bin/env python3

import sys

input_file = "test.txt"
#input_file = "test2.txt"
#input_file = "input.txt"

with open(input_file) as f:
    data = f.read().splitlines()


headings = {0:'E', 90:'S', 180:'W', 270:'N'}
headings2 = {'E':0, 'S':90, 'W':180, 'N':270}

class Boat:
    def __init__(self,x,y,heading):
        self.x = x
        self.y = y
        self.heading = heading

    def printB(self):
        print("Boat is at {},{}, heading {}, aka {}".format(self.x, self.y, self.heading, headings[self.heading]))

    def move(self, heading, amount):
        if heading == 'N':
            self.y += amount
        elif heading == 'S':
            self.y -= amount
        elif heading == 'E':
            self.x += amount
        elif heading == 'W':
            self.x -= amount

    def turn(self, direction, amount):
        if direction == "R":
            self.heading = (self.heading + amount) % 360
        elif direction == "L":
            self.heading = (self.heading - amount) % 360

    def forward(self, amount):
        self.move(headings[self.heading], amount)




b = Boat(0,0,0)
b.printB()

for d in data:
    if d[0] in ['N', 'S', 'E', 'W']:
        b.move(d[0], int(d[1:]))
    elif d[0] in ['L', 'R']:
        b.turn(d[0], int(d[1:]))
    elif d[0] == 'F':
        b.forward(int(d[1:]))

b.printB()
print("PART1: Boat is {} from start".format(abs(b.x)+abs(b.y)))
