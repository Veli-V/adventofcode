import math
import os

#path = "test4.txt"
path = "input.txt"



inputFile = open(path)
intcode = inputFile.readline()
rounds = 0
number1 = 0
number2 = 0
toStore = 0
answer = 0


intcode = str.split(intcode, ',')
print(intcode)
while True:
    command = int(intcode[rounds])
    print(command)
    if command == 1:
        number1 = int(intcode[rounds + 1])
        number1 = int(intcode[number1])
        number2 = int(intcode[rounds + 2])
        number2 = int(intcode[number2])
        toStore = int(intcode[rounds + 3])
        answer = number1 + number2
        intcode[toStore] = answer
        rounds += 4
        print("number1 = " + str(number1) + " number2 = " + str(number2) + " eli kokonaan:")
        print(intcode)
    elif command == 2:
        number1 = int(intcode[rounds + 1])
        number1 = int(intcode[number1])
        number2 = int(intcode[rounds + 2])
        number2 = int(intcode[number2])
        toStore = int(intcode[rounds + 3])
        answer = number1 * number2
        intcode[toStore] = answer
        rounds += 4
        print("number1 = " + str(number1) + " number2 = " + str(number2) + " eli kokonaan:")
        print(intcode)
    elif command == 99:
        break
        print(intcode)
    else:
        print("panic, rikki meni")
        break

print("Vastaus on: " + str(intcode[0]))
