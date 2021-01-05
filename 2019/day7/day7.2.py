import math
import os
from itertools import permutations

path = "test4.txt"
path = "input.txt"




stepcounts = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4, 99:0}

parameterMode = False
location = 0
opCode = '0'
#print(intcode)
jumped = False
lastOutput = 0
inputCount = 0
beakPower = 0
memory = []

def resetMemory():
    memory.clear()
    for i in range(5):
        inputFile = open(path)
        intcode = inputFile.readline()
        intcode = intcode.strip()
        intcode = intcode.split(',')
        memory.append(intcode.copy())

#print(memory)

def runIntcode(codePath, queue, pc, location = 0):
    #print("nyt ajossa muistilla, jonolla, pc, lokaatiolla:")
    #print(str(codePath) + " " + str(queue) + " " + str(pc)+ " "  + str(location))
    parameterMode = False
    #location = 0
    opCode = '0'
    #print(intcode)
    jumped = False
    lastOutput = 0
    inputCount = 0
    intcode = codePath
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
            if opCode in [1,2,5,6,7,8]:
                pos2 = location + 2 if parameterMode and b == 1 else int(intcode[location+2])
            if opCode in [1,2,7,8]:
                pos3 = int(intcode[location+3])

        if opCode == 1:
            intcode[pos3] = int(intcode[pos1]) + int(intcode[pos2])
        elif opCode == 2:
            intcode[pos3] = int(intcode[pos1]) * int(intcode[pos2])
        elif opCode == 3:
            #intcode[pos1] = input()
            #print("in 3 " + str(queue))
            intcode[pos1] = queue.pop(0)
        elif opCode == 4:
            #print(intcode[pos1])
            lastOutput = intcode[pos1]
            #print("in 4 " + str(queue))
            return lastOutput, pc+1, location+step
        elif opCode == 5:
            if (int(intcode[pos1]) != 0):
                location = int(intcode[pos2])
                jumped = True
        elif opCode == 6:
            if (int(intcode[pos1]) == 0):
                location = int(intcode[pos2])
                jumped = True
        elif opCode == 7:
            intcode[pos3] = 1 if int(intcode[pos1]) < int(intcode[pos2]) else 0
        elif opCode == 8:
            intcode[pos3] = 1 if intcode[pos1] == intcode[pos2] else 0
        elif opCode == 99:
            #print("loppuun päästiin")
            return None, -1, 0
        else:
            print("Vituiks män, paniikki jne jne.")
        #print(intcode)
        if not jumped:
            location += step
        jumped = False

possibleInputs = [5,6,7,8,9]
beakCombo = possibleInputs
#print(lastOutput)
#lastOutput = runIntcode(path, 3, 0)
#print(lastOutput)
lastOutput = 0
for combo in permutations(possibleInputs,5):
    resetMemory()
    power = 0
    #print("permutaatiolla: " + str(combo))
    q = [ [0] for _ in range(len(combo)) ]
    loc = [0, 0, 0, 0, 0]
    for i in range(len(combo)):
        q[i][0] = combo[i]
    pc = 0
    q[0].append(0)
    #print(q)
    #print(loc)
    while pc >= 0:
        #print(loc)
        lastOutput, pc, newLocation = runIntcode(memory[pc], q[pc], pc, loc[pc])
        if pc > 4:
            pc = 0
        if lastOutput != None:
            q[pc].append(lastOutput)
            power = lastOutput
        loc[pc-1] = newLocation
        #print("last output: " + str(lastOutput) + " pc " + str(pc) + " uusi lokaatio: " + str(newLocation) + " ja jono: " + str(q[pc]))
        #print(memory)
        if pc == -1:
            #print("kierros valmis")
            #print("tällä permutaatiolla teho: " + str(power))
            break
    if power > beakPower:
        beakPower = power
        beakCombo = combo

print("beak power: " + str(beakPower) + " with combo: " + str(beakCombo))
