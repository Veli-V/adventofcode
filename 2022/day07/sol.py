#!/usr/bin/env python3
import sys

class Dir:
    def __init__(self, name, dirs, files, parent):
        self.name = name
        self.dirs = dirs
        self.files = files
        self.parent = parent

    def fileAdd(self, file):
        self.files.append(file)

    def dirAdd(self,dir):
        self.dirs.append(dir)

    def getSize(self, smalls, biggs, bsize):
        size = 0
        for f in self.files:
            size += int(f)
        for d in self.dirs:
            tmp, smalls, biggs = d.getSize(smalls, biggs, bsize)
            if tmp < 100000:
                #print("Folder that matches: {}: {}".format(d.getName(), tmp))
                smalls.append(d)
            elif tmp > bsize:
                biggs.append(d)
            size += tmp
            #print(smalls)
        return size, smalls, biggs

    def print(self):
        print("Directory {}".format(self.name))
        print("Dirs:")
        for d in self.dirs:
            print("{}:{}".format(d.getName(), d))
        print("Files:")
        for f in self.files:
            print(f)
        print("Parent:")
        print(self.parent)

    def getName(self):
        return self.name

    def getDir(self, dir):
        for d in self.dirs:
            if d.getName() == dir:
                return d
        #print("Ei löytynynnä kansioo")
        #print(dir)
        #self.print()


    def getParent(self):
        return self.parent


input_file = 'test_input.txt'
input_file = 'input.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]
#print(data)

rootDir = Dir("/", [], [], '')
#rootDir.print()
currentDir = rootDir

for d in data:
    d = d.split(" ")
    #print(d)
    if d[0] == '$':
        reading = False
        if d[1] == 'cd':
            if d[2] == '/':
                currentDir = rootDir
            elif d[2] == '..':
                currentDir = currentDir.getParent()
            else:
                currentDir = currentDir.getDir(d[2])
                #currentDir.print()
        elif d[1] == 'ls':
            reading = True

    elif reading:
        if d[0] == 'dir':
            #print("Reading dir: cd {} dir {}".format(currentDir, d[1]))
            tmpDir = Dir(d[1], [], [], currentDir)
            currentDir.dirAdd(tmpDir)
        else:
            currentDir.fileAdd(d[0])

needed, smals, bigs = rootDir.getSize([], [], 70000000)
needed = 70000000 - needed
needed = 30000000 - needed
size, smalls, biggs = rootDir.getSize([], [], needed)

sum = 0
bigs = []
for s in smalls:
    size, smalls, bigs = s.getSize([], [], needed)
    sum += size
print("Part1:")
print("Sum of dirs below 100 000: {}".format(sum))
sb = 3030000000

for b in biggs:
    #print(b.getName())
    size, smalls, bigs = b.getSize([], [], needed)
    #print("bigs now: {}, size {}, needed {}".format(b.getName(), size, needed))
    if size < sb:
        sb = size


print("Part2:")
print("Smallest big folders size: {}".format(sb))
