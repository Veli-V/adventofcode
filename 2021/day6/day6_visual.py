#!/usr/bin/env python3
import sys
from graphics import *
from time import sleep
import random
#input_file = 'test_input.txt'
#input_file = 'onefish.txt'
input_file = 'input.txt'

days = 256


with open(input_file) as f:
    data = f.readlines()
data = [int(n) for n in data[0].split(",")]

fisuja = [0,0,0,0,0,0,0,0,0]

colors = ["red", "green", "gold", "yellow", "purple"]
win = GraphWin("fish", 1024, 1024)
bcirc = Circle(Point(512,512), 4)
bcirc.setFill("gold")
bcirc.draw(win)
day = Text(Point(500,25), "0")
day.draw(win)



for d in data:
    fisuja[d] += 1

for i in range(int(sum(fisuja)/10)):
    x = randrange(-4,4)
    y = randrange(-4,4)
    win.plot(512+x, 512+y, colors[abs(x)])

for i in range(days):
    day.setText(str(i))
    tmp = fisuja[0]
    for j in range(6):
        fisuja[j] = fisuja[j+1]

    fisuja[6] = tmp + fisuja[7]
    fisuja[7] = fisuja[8]
    fisuja[8] = tmp
    bcirc.undraw()
    bcirc = Circle(Point(512,512), 4*i)
    bcirc.draw(win)
    time.sleep(0.1)
    for j in range(int(fisuja[8]/10)):
        x = randrange(-4*i,4*i)
        y = randrange(-4*i,4*i)
        col = randrange(0,4)
        win.plot(512+x, 512+y, colors[col])
    #time.sleep(0.1)

print("PART2:" + str(sum(fisuja)))
time.sleep(1)
win.getMouse()
win.close()
