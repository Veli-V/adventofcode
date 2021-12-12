#!/usr/bin/env python3

# Disclaimer: I haven't made this ugly code for a while,
# but this was solved during cottage weekend with more than
# couple of beers
import sys
import string

class node:

    def __init__ (self, name):
        self.connections = []
        if 1 in [c in string.ascii_lowercase for c in name]:
            self.minor = True
        else:
            self.minor = False
        self.name = name

    def addConnection (self, connection):
        self.connections.append(connection)

    def findRoute(self, route):
        # part 1
        #if self.minor and self.name in route:
            #return

        #Part 2
        if self.minor and self.name in route and duplicateMinors(route):
            return

        route.append(self.name)
        #self.print()
        #print(route)
        if self.name == "end":
            routes.append(route)
            #print(routes)
            return

        for c in self.connections:
            if c == "start":
                continue
            #print("we are in {} and going to {}".format(self.name, c))
            nodes[c].findRoute(route.copy())
        return

    def print(self):
        print("node: {} ".format(self.name))
        print("Connections {}".format(self.connections))

    def isMinor(self):
        return self.minor


def duplicateMinors(route):
    seen = []
    for r in route:
        if nodes[r].isMinor() and r in seen and r not in ["start", "end"]:
            return True
        elif nodes[r].isMinor:
            seen.append(r)
    return False


input_file = 'test_input.txt'
input_file = 'test_input2.txt'
input_file = 'test_input3.txt'
input_file = 'input.txt'
#input_file = 'easymode'
#

routes = []
nodes = {}

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

for d in data:
    if d.split("-")[0] not in nodes.keys():
        tmpNode = node(d.split("-")[0])
        nodes[d.split("-")[0]] = tmpNode
    if d.split("-")[1] not in nodes.keys():
        tmpNode = node(d.split("-")[1])
        nodes[d.split("-")[1]] = tmpNode
    nodes[d.split("-")[0]].addConnection(d.split("-")[1])
    nodes[d.split("-")[1]].addConnection(d.split("-")[0])

nodes["start"].findRoute([])

#for r in routes:
    #print(r)
print("We found {} routes".format(len(routes)))
