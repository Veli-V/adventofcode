import math
import os

#path = "test3.txt"
path = "input.txt"



inputFile = open(path)
intcode = inputFile.readline()
intcode = intcode.strip()
intcode = intcode.split(',')

stepcounts = {1:4, 2:4, 3:2, 4:2, 99:0}

parameterMode = False
location = 0
opCode = '0'
#print(intcode)

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
        if opCode in [1,2]:
            pos2 = location + 2 if parameterMode and b == 1 else int(intcode[location+2])
        if opCode in [1,2]:
            pos3 = int(intcode[location+3])

    if opCode == 1:
        intcode[pos3] = int(intcode[pos1]) + int(intcode[pos2])
    elif opCode == 2:
        intcode[pos3] = int(intcode[pos1]) * int(intcode[pos2])
    elif opCode == 3:
        intcode[pos1] = input()
    elif opCode == 4:
        print(intcode[pos1])
    elif opCode == 99:
        print("loppuun päästiin")
        break
    else:
        print("Vituiks män, paniikki jne jne.")
    #print(intcode)
    location += step


print(intcode[0])
