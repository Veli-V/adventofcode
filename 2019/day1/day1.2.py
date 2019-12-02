import math
import os

def countGas( mass ):
    gas = 0;
    gas = int(mass) / 3
    gas = math.floor(gas)
    gas = gas - 2
    gas2 = 0
    if gas > 0:
        gas2 = countGas(gas)
    if gas2 >= 0:
        gas += gas2
    return gas

gasAll = 0
with open('input.txt') as file:
    for line in file:
        gas = countGas(line)
        #print("for line " + str(line) + " answer is " + str(gas))
        gasAll += gas
print(gasAll)

