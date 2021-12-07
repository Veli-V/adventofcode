#!/usr/bin/env python3
import sys
from graphics import *
from time import sleep

#input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

numerot = data[0]
numerot = numerot.split(',')
laput = []
tmpLappu = []

kierros = 1

for i in range(1,len(data)):
    if kierros == 6:
        tmpLappu.append(data[i])
        tmpBingo = bingo_ruutu(tmpLappu.copy())
        #laput.append(bingo_ruutu(tmpLappu.copy()))
        laput.append(tmpBingo)
        del tmpBingo
        tmpLappu.clear()
        kierros = 1
    else:
        tmpLappu.append(data[i])
        kierros +=1

class bingo_ruutu:

    def __init__(self, rows):
        self.rivit = []
        self.voittanut = False
        tmpRow = []
        for r in rows:
            for i in r.split():
                tmpRow.append(i)
            self.rivit.append(tmpRow.copy())
            tmpRow.clear()
        del self.rivit[0]

    def print(self):
        print("lappu:")
        for r in self.rivit:
            print(r)

    def find(self, n):
        if (self.voittanut):
            return False, -1, -1
        for i in range(5):
            for j in range(5):
                if self.rivit[i][j] == n:
                    self.rivit[i][j] = -1
                    voitto = True
                    for k in range(5):
                        if self.rivit[i][k] != -1:
                            voitto = False
                            break
                    if not voitto:
                        voitto = True
                        for k in range(5):
                            if self.rivit[k][j] != -1:
                                voitto = False
                                break
                    self.voittanut = voitto
                    return voitto, i, j
        return False, -1, -1


    def count(self):
        sum = 0
        for r in self.rivit:
            for n in r:
                if n != -1:
                    sum += int(n)
        return sum



def bingo(win, rects, number, circs):

    voittoja = 0
    for n in numerot:
        for l in laput:
            number.setText(str(n))
            win.update()
            voittiko, x, y = l.find(n)
            indexi = laput.index(l)
            if x != -1:
                circs[indexi][x][y].setFill("green")
            if(voittiko and voittoja == 0):
                voittavaLappu = l
                voittavaNumero = n
                voittoja += 1
                colorRect(win, rects[indexi], 1)
            elif(voittiko and voittoja == len(laput)-1):
                vikaVoittavaLappu = l
                vikaVoittavaNumero = n
                colorRect(win, rects[indexi], 3)
                break
            elif(voittiko):
                voittoja +=1
                colorRect(win, rects[indexi], 2)
            #time.sleep(0.1)
        else:
            continue
        break


    print("eka voittava lappu:")
    voittavaLappu.print()
    print(voittavaLappu.count())
    print(voittavaNumero)
    print(str(voittavaLappu.count() * int(voittavaNumero)))
    print("vika voittava lappu:")
    vikaVoittavaLappu.print()
    print(vikaVoittavaLappu.count())
    print(vikaVoittavaNumero)
    print(str(vikaVoittavaLappu.count() * int(vikaVoittavaNumero)))

def colorRect(win, rect, order):
    if order == 1:
        rect.setFill("gold")
    elif order == 2:
        rect.setFill("silver")
    else:
        rect.setFill("gray")
    win.update()
    time.sleep(0.1)


def main():
    size = math.ceil(math.sqrt(len(laput)))
    win = GraphWin("bingo", size*100,size*100+10)
    row, column = -1,0
    rects = []
    number = Text(Point((size/2)*100, 10), "")
    number.draw(win)
    acircs = []

    # prerpare the bingo table
    for i in range(len(laput)):
        if i % size == 0:
            row += 1
            column = 0
        upperpt = Point(10+column*100, row*100+20)
        lowerpt = Point((column+1)*100-10, (row+1)*100)
        rect = Rectangle(upperpt, lowerpt)
        rects.append(rect)
        rect.draw(win)
        circs = []
        tmpCircs = []

        for k in range(1,6):
            for z in range(1,6):
                circ = Circle(Point(upperpt.getX() + z*13+2, upperpt.getY() + k*13+2), 4)
                circ.draw(win)
                tmpCircs.append(circ)
            circs.append(tmpCircs.copy())
            tmpCircs.clear()

        column += 1
        acircs.append(circs.copy())
    win.getMouse()
    bingo(win, rects, number, acircs)
    win.getMouse()
    win.close()
    print("done")


if __name__ == __name__:
    main()
