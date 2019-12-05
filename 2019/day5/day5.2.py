import math
import os

path = "test4.txt"
path = "input.txt"



inputFile = open(path)
intcode = inputFile.readline()
intcode = intcode.strip()
intcode = intcode.split(',')

stepcounts = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 99:0}

parameterMode = False
location = 0
opCode = '0'
#print(intcode)
jumped = False

while True:
    command = str(intcode[location])
    if len(command) < 2:
        parameterMode = False
        opCode = int(intcode[location])
        #print("simple code is: " + str(opCode))
    else:
        parameterMode = True
        opCode = int(command[-2:])
        a = int(command[-3:-2] if len(command) >= 3 else 0)
        b = int(command[-4:-3] if len(command) >= 4 else 0)
        c = int(command[-5:-4] if len(command) >= 5 else 0)
        #print("not so simple code is: " + str(opCode))
        #print("with parameters:")
        #print("a: " + str(a) + " b: " + str(b) + " c: " + str(c))
    step = stepcounts[opCode]    

    # input ja output lokaatiot:
    if opCode not in [99]:
        pos1 = location + 1 if parameterMode and a == 1 else int(intcode[location+1])
        if opCode in [1,2,5,6,7,8]:
            pos2 = location + 2 if parameterMode and b == 1 else int(intcode[location+2])
        if opCode in [1,2,7,8]:
            pos3 = int(intcode[location+3])

    if opCode == 1:
        intcode[pos3] = int(intcode[pos1]) + int(intcode[pos2])
    elif opCode == 2:
        intcode[pos3] = int(intcode[pos1]) * int(intcode[pos2])
    elif opCode == 3:
        intcode[pos1] = input()
    elif opCode == 4:
        print(intcode[pos1])
    elif opCode == 5:
        if (int(intcode[pos1]) != 0):
            location = int(intcode[pos2])
            jumped = True
    elif opCode == 6:
        if (int(intcode[pos1]) == 0):
            location = int(intcode[pos2])
            jumped = True
    elif opCode == 7:
        intcode[pos3] = 1 if intcode[pos1] < intcode[pos2] else 0
    elif opCode == 8:
        intcode[pos3] = 1 if intcode[pos1] == intcode[pos2] else 0
    elif opCode == 99:
        print("loppuun päästiin")
        break
    else:
        print("Vituiks män, paniikki jne jne.")
    #print(intcode)
    if not jumped:
        location += step
    jumped = False


print(intcode[0])
