import math
import os

#path = "test4.txt"
path = "input.txt"


rightAnswer = 19690720

inputFile = open(path)
intcode = inputFile.readline()
rounds = 0
number1 = 0
number2 = 0
toStore = 0
answer = 0


intcode = str.split(intcode, ',')
original = intcode.copy()
print(original)

for i in range(0,100):
    for j in range(0,100):
        intcode.clear()
        intcode = original.copy()
        intcode[1] = i
        intcode[2] = j
        #print("kierros: i=" + str(i) + " j=" + str(j))
        #print(intcode)
        #print(original)
        rounds = 0
        while True:
            command = int(intcode[rounds])
            #print(command)
            if command == 1:
                number1 = int(intcode[rounds + 1])
                number1 = int(intcode[number1])
                number2 = int(intcode[rounds + 2])
                number2 = int(intcode[number2])
                toStore = int(intcode[rounds + 3])
                answer = number1 + number2
                intcode[toStore] = answer
                rounds += 4
                #print("number1 = " + str(number1) + " number2 = " + str(number2) + " eli kokonaan:")
                #print(intcode)
            elif command == 2:
                number1 = int(intcode[rounds + 1])
                number1 = int(intcode[number1])
                number2 = int(intcode[rounds + 2])
                number2 = int(intcode[number2])
                toStore = int(intcode[rounds + 3])
                answer = number1 * number2
                intcode[toStore] = answer
                rounds += 4
                #print("number1 = " + str(number1) + " number2 = " + str(number2) + " eli kokonaan:")
                #print(intcode)
            elif command == 99:
                break
                #print(intcode)
            else:
                print("panic, rikki meni")
                break
        answer = intcode[0]
        #print(intcode)
        #print(answer)
        if answer == rightAnswer:
            break
    if answer == rightAnswer:
        break

print("Vastaus on: " + str(intcode[0]))
print("joilloin arvot on: noun " + str(intcode[1]) + " ja verb " +str(intcode[2]))
answer = 100 * intcode[1] + intcode[2]
print(answer)
