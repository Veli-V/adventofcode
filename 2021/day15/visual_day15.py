#!/usr/bin/env python3

import sys
import pygame
from queue import PriorityQueue

#input_file = 'test_input.txt'
input_file = 'input.txt'
#input_file = 'simple.txt'

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
width = len(data[0])
height = len(data)
oldPath = {}


SQUARESIZE = 5
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GREY = (100, 100, 100)
WINDOW_HEIGHT = height*SQUARESIZE
WINDOW_WIDTH = width*SQUARESIZE
positions = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        positions[(j,i)] = int(data[i][j])

def hDist(pos, greed = 1):
    return (width - 1 - pos[0])*greed + (height - 1 - pos[1]*greed)

def inBounds(pos):
    x,y = pos
    if x < 0 or x > width-1 or y < 0 or y > height -1:
        return False
    return True

def neighbors(pos):
    result = []
    x,y = pos
    nn = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for n in nn:
        if inBounds(n):
            result.append(n)
    return result

def reconstructPath(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path


def findRoute(start, part2 = False, greed = 1):
    global width
    global height
    def cost(pos):
        x, y = pos
        if not part2:
            return positions[pos]
        else:
            result = positions[(x % tilewidth, y % tileheight)] + int(x // tilewidth) + int(y // tileheight)
            if result > 9:
                return result % 9
            else:
                return result
    q = PriorityQueue()
    cameFrom = {}
    path = {}
    qq = {}
    path[start] = 0
    tilewidth, tileheight = width, height
    if part2:
        width *= 5
        height *= 5
    goal = (width-1, height-1)


    q.put((0, start))
    qq[start] = 0
    newpath = {}

    while not q.empty():
        current = q.get()
        #print("del from qq {}".format(current[1]))
        qq.pop(current[1], None)
        if current[1] == goal:
            print(path[goal])
            return path[goal]
        for nn in neighbors(current[1]):
            maybeCost = path[current[1]] + cost(nn)
            if nn not in path or maybeCost < path[nn]:
                cameFrom[nn] = current[1]
                path[nn] = maybeCost
                newpath[nn] = 0
                prio = maybeCost + hDist(nn, greed)
                q.put((prio, nn))
                #print("add to qq {}".format(nn))
                qq[nn] = 0
            #changed = drawGrid(path, qq,[current[1]])
            changed = drawGrid(newpath, qq, reconstructPath(cameFrom, current[1]))
            qq.clear()
            newpath.clear()
            pygame.display.update(changed)
    print("Failas")

def main():
    global SCREEN, CLOCK, SQUARESIZE
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    path = []
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_a:
                    findRoute((0,0), False, 2)
                if event.key == pygame.K_s:
                    findRoute((0,0), False, 1)
                if event.key == pygame.K_d:
                    SQUARESIZE = SQUARESIZE // 5
                    #SCREEN = pygame.display.set_mode((WINDOW_WIDTH*5, WINDOW_HEIGHT*5))
                    findRoute((0,0), True, 5)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



def drawGrid(visited, q, path):
    global oldPath
    blocksize = SQUARESIZE #Set the size of the grid block
    changed = []
    #for x in range(0, WINDOW_WIDTH, blockSize):
    #    for y in range(0, WINDOW_HEIGHT, blockSize):
    #        rect = pygame.Rect(x, y, blockSize, blockSize)
    #        if (int(x/SQUARESIZE),int(y/SQUARESIZE)) in q:
    #            pygame.draw.rect(SCREEN, RED, rect, 0)
    #            changed.append(rect)
    #        elif (int(x/SQUARESIZE),int(y/SQUARESIZE)) in path:
    #            pygame.draw.rect(SCREEN, GREEN, rect, 0)
    #            changed.append(rect)

    #        elif (int(x/SQUARESIZE),int(y/SQUARESIZE)) in visited:
    #            pygame.draw.rect(SCREEN, GREY, rect, 0)
    #            changed.append(rect)
    #        pygame.draw.rect(SCREEN, WHITE, rect, 1)
    for x,y in oldPath:
        rect = pygame.Rect(x*SQUARESIZE, y*SQUARESIZE, blocksize, blocksize)
        pygame.draw.rect(SCREEN, GREY, rect, 0)
        changed.append(rect)
    #for x,y in visited:
    #    rect = pygame.Rect(x*SQUARESIZE, y*SQUARESIZE, blocksize, blocksize)
    #    pygame.draw.rect(SCREEN, GREY, rect, 0)
    #    changed.append(rect)
    for x,y in q:
        rect = pygame.Rect(x*SQUARESIZE, y*SQUARESIZE, blocksize, blocksize)
        pygame.draw.rect(SCREEN, RED, rect, 0)
        changed.append(rect)
    for x,y in path:
        rect = pygame.Rect(x*SQUARESIZE, y*SQUARESIZE, blocksize, blocksize)
        pygame.draw.rect(SCREEN, GREEN, rect, 0)
        changed.append(rect)
    oldPath = path.copy()

    return changed

if __name__ == '__main__':
    main()
