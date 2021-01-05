#!/usr/bin/env python3
import sys
import math

#input_file = "test.txt"
#input_file = "test2.txt"
input_file = "input.txt"

with open(input_file) as f:
    data = f.read().splitlines()


headings = {0:'E', 90:'S', 180:'W', 270:'N'}
headings2 = {'E':0, 'S':90, 'W':180, 'N':270}


def rotatePoint(centerPoint,point,angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

class Boat:
    def __init__(self,x,y,heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.wx = 10
        self.wy = 1

    def printB(self):
        print("Boat is at {},{}, waypoint is {},{}".format(self.x, self.y, self.wx, self.wy))

    def moveW(self, heading, amount):
        if heading == 'N':
            self.wy += amount
        elif heading == 'S':
            self.wy -= amount
        elif heading == 'E':
            self.wx += amount
        elif heading == 'W':
            self.wx -= amount

    def turn(self, direction, amount):
        if direction == 'R':
            amount = 360 - amount
        x = rotatePoint([0,0], [self.wx, self.wy], amount)
        self.wx = x[0]
        self.wy = x[1]


    def move(self, amount):
        self.x += amount * self.wx
        self.y += amount * self.wy

    def forward(self, amount):
        self.move(amount)




b = Boat(0,0,0)
b.printB()

for d in data:
    if d[0] in ['N', 'S', 'E', 'W']:
        b.moveW(d[0], int(d[1:]))
    elif d[0] in ['L', 'R']:
        b.turn(d[0], int(d[1:]))
    elif d[0] == 'F':
        b.forward(int(d[1:]))

b.printB()


print("PART2: Boat is {} from start".format(abs(b.x)+abs(b.y)))
