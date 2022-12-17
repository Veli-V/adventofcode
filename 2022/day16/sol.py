#!/usr/bin/env python3
import sys

input_file = 'test_input.txt'
#input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

class Cave():
    def __init__(self,name, flowrate, routes):
        self.name = name
        self.flowrate = flowrate
        self.routes = routes
        self.overallflow = 0
        self.isopen = False

    def getPotential(self, time):
        return time*self.flowrate

    def __str__(self):
        return "cave {}, flowrate {}, flow {}, available routes {}".format(self.name, self.flowrate, self.overallflow, self.routes)


start = "AA"
timer = 30
closed, opened, routes = {}, {}, []
for d in data:
    d = d.split(" ")
    name = d[1]
    rate = int(d[4].split("=")[1].strip(";"))
    for i in range(9, len(d)):
        routes.append(d[i].strip(","))
    tmpCave = Cave(name, rate, routes.copy())
    closed[name] = tmpCave
    routes.clear()

for n in closed:
    print (closed[n])
