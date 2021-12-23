#!/usr/bin/env python3

#test:
#target area: x=20..30, y=-10..-5
#target area: x=281..311, y=-74..-54

#targetX = range(20, 31)
#targetY = range(-10, -4)
targetX = range(281, 312)
targetY = range(-74,-53)


def inGoal(x,y):
    return x in targetX and y in targetY

pos = 0
possibleX = []
possibleY = []
for x in range(max(targetX)+1):
    pos = 0
    #print("kokeillaan arvoa {}".format(x))
    for i in reversed(range(x+1)):
        pos += i
        #print("Nyt arvolla {}, nopeus nyt {}, sijainti {}".format(x, i, pos))
        if pos in (targetX):
            #print("osui maaliin, x= {}, pos={}".format(x, pos))
            possibleX.append(x)
            break
        if pos > max(targetX):
            break
print(possibleX)

for y in range(0-max(abs(max(targetY)+1), abs(min(targetY))), max(abs(max(targetY)+1), abs(min(targetY)))):
    pos = 0
    speed = y
    while pos >= min(targetY):
        pos += speed
        speed -= 1
        if pos in targetY:
            possibleY.append(y)
            break

print(possibleY)

maxH = 0
posx = 0
posy = 0
starts = set()
for x in possibleX:
    for y in possibleY:
        posx = 0
        posy = 0
        ySpeed = y
        xSpeed = x
        while posy > min(targetY):
            posx += xSpeed
            posy += ySpeed
            xSpeed -= 1 if xSpeed > 0 else 0
            ySpeed -= 1
            if posy > maxH:
                maxH = posy
                maxX, maxY = x, y
            if inGoal(posx, posy):
                starts.add((x,y))

print("PART1: with start of {}:{}, max height {}".format(maxX, maxY, maxH))
print(len(starts))
print(starts)
