#!/usr/bin/env python3
import sys

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
            return False
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
                    return voitto


    def count(self):
        sum = 0
        for r in self.rivit:
            for n in r:
                if n != -1:
                    sum += int(n)
        return sum


#input_file = 'ptest.txt'
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

voittoja = 0
for n in numerot:
    for l in laput:
        voittiko = l.find(n)
        if(voittiko and voittoja == 0):
            voittavaLappu = l
            voittavaNumero = n
            voittoja += 1
        elif(voittiko and voittoja == len(laput)-1):
            vikaVoittavaLappu = l
            vikaVoittavaNumero = n
        elif(voittiko):
            voittoja +=1

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
