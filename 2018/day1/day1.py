import os
import sys

sum = 0
taajuudet = [0]*1000000
duplikaatti = True
while(duplikaatti) :
    f = open('input1.txt', 'r')
    for line in f:
        sum = sum + int(line)
        #print(str(sum))
        #for taajuus in taajuudet:
        #    if sum == taajuus:
        #        print('duplikaatti löytyi, se on: ' + str(sum))
        #        duplikaatti = False
        #        break
        #taajuudet.append(sum)
        if taajuudet[sum] == 1:
            print('duplikaatti löytyi, se on: ' + str(sum))
            duplikaatti = False
            break
        taajuudet[sum] = 1
    f.close()
    print('lopullinen summa: ' + str(sum))
