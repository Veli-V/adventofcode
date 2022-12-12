#!/usr/bin/env python3
import copy
import sys

input_file = 'test_input.txt'
#input_file = 'one.txt'
input_file = 'input.txt'

rounds1 = 20
rounds2 = 10000

class Monkey:
    def __init__(self, name, items, operation, opby, divby, toTrue, toFalse):
        self.name = name
        self.items = copy.deepcopy(items)
        self.operation = operation
        self.opby = opby
        self.divby = divby
        self.toTrue = toTrue
        self.toFalse = toFalse
        self.inspects = 0

    def print(self):
        print(self.name)
        print("Items: {}".format(self.items))
        print("operation: {} {}".format(self.operation, self.opby))
        print("Check againts: {}".format(self.divby))
        print("If true: {}, if false {}".format(self.toTrue, self.toFalse))

    def receive(self, item):
        self.items.append(item)

    def inspect(self, part1):
        while len(self.items) > 0:
            i = self.items.pop(0)
            self.inspects += 1
            #print("inspecting item {} with op {} {}".format(i, self.operation, self.opby), end=" ")
            if(self.opby != "old"):
                if self.operation == "+": i += int(self.opby)
                if self.operation == "*": i = i*int(self.opby)
            else:
                if self.operation == "+": i += i
                if self.operation == "*": i *= i
            #print("it changed to {}".format(i), end=" ")
            if part1:
                i = int(i/3)
            else:
                i = i % commondiv
            #print("div by three {}.".format(i))
            #print("is item div by {}, thats {}".format(self.divby, i % self.divby == 0 ), end=" ")
            if i%self.divby == 0:
                #print("Sending to {}".format(self.toTrue))
                monkeys[self.toTrue].receive(i)
            else:
                #print("Sending to {}".format(self.toFalse))
                monkeys[self.toFalse].receive(i)


    def printItems(self):
        print(self.name, end=": ")
        print(self.items)
        print()


if len(sys.argv) >  1 :
    input_file = sys.argv[1]

items, monkeys = [], []
commondiv = 1

with open(input_file) as f:
    while(True):
        line = f.readline()
        if line:
            items.clear()
            name = line.strip()
            line = f.readline()
            line = line.split(" ")
            for i in range(4, len(line)):
                items.append(int(line[i].strip(",")))
            line = f.readline().split(" ")
            operation = line[6]
            opby = line[7].strip()
            line = f.readline()
            line = line.split(" ")
            divby = int(line[5])
            commondiv *= divby
            line = f.readline().split(" ")
            toTrue = int(line[9].strip())
            line = f.readline().split(" ")
            toFalse = int(line[9].strip())
            monkeys.append(Monkey(name, items, operation, opby, divby, toTrue, toFalse))
            f.readline()

        else:
            break

#for m in monkeys:
#    m.print()

#for i in range(rounds1):
#    #print("After {} rounds".format(i))
#    for m in monkeys:
#        m.inspect(True)
#        #m.print()
#    #for m in monkeys:
#    #    m.printItems()

#maxi, smaxi = 0,0
#for m in monkeys:
#    #m.print()
#    print("{} inspected {}".format(m.name, m.inspects))
#    if m.inspects > maxi:
#        smaxi = maxi
#        maxi = m.inspects
#    elif m.inspects > smaxi:
#        smaxi = m.inspects
#
#print("Most monkey business was {} and {}, so {}".format(maxi, smaxi, maxi*smaxi))

for i in range(rounds2):
    if i in [1, 20] or i % 1000 == 0:
        print("After {} rounds: ".format(i))
    for m in monkeys:
        m.inspect(False)
        if i in [1, 20] or i % 1000 == 0:
            print("{} inspected {}".format(m.name, m.inspects))


maxi, smaxi = 0,0
for m in monkeys:
    print("{} inspected {}".format(m.name, m.inspects))
    if m.inspects > maxi:
        smaxi = maxi
        maxi = m.inspects
    elif m.inspects > smaxi:
        smaxi = m.inspects

print("Most monkey business was {} and {}, so {}".format(maxi, smaxi, maxi*smaxi))
