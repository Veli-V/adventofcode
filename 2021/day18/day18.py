#!/usr/bin/env python3

import sys
import math

sys.setrecursionlimit(1000)

class snailfish:
    def __init__(self):
        self.left = ""
        self.right = ""
        self.parent = ""

    def set(self, l, r):
        self.left = l
        self.right = r

    def getL(self):
        return self.left
    def getR(self):
        return self.right

    def setParent(self, par):
        self.parent = par

    def childParent(self):
        if isinstance(self.left, snailfish):
            self.left.setParent(self)
        if isinstance(self.right, snailfish):
            self.right.setParent(self)


    def print(self):
        print("[", end = "")
        if isinstance(self.left, snailfish):
            self.left.print()
        else:
            print(self.left, end="")
        print(",", end="")
        if isinstance(self.right, snailfish):
            self.right.print()
        else:
            print(self.right, end="")
        print("]", end="")

    def add(self, sf):
        self.left = self
        self.right = sf

    def explode(self):
        print("räjähti")
        self.print()
        print()
        findNextLeft(self, self.parent, self.left)
        findNextRight(self, self.parent, self.right)
        self.parent.zero(self)

    def zero(self, s):
        if self.left == s:
            self.left = 0
        elif self.right == s:
            self.right = 0
        else:
            print("Jotain kusahti zerossa")

    def reduce(self, d):
        exp, split = True, True
        while exp or split:
            exp = self.checkExplode(0)
            split = self.checkSplit()
            print("exp: {}, split {}".format(exp, split))

    def checkSplit(self):
        splitHappened = False
        if isinstance(self.left, int) and self.left > 9:
            tmp = self.left
            tmpl = math.floor(tmp/2)
            tmpr = math.ceil(tmp/2)
            tmp = snailfish()
            tmp.set(tmpl, tmpr)
            tmp.setParent(self)
            self.left = tmp
            return True
        elif isinstance(self.right, int) and self.right > 9:
            tmp = self.right
            tmpl = math.floor(tmp/2)
            tmpr = math.ceil(tmp/2)
            tmp = snailfish()
            tmp.set(tmpl, tmpr)
            tmp.setParent(self)
            self.right = tmp
            return True
        if isinstance(self.left, snailfish):
            splitHappened =  self.left.checkSplit()
        if isinstance(self.right, snailfish) and not splitHappened:
            splitHappened =  self.right.checkSplit()
        self.print()
        print("Ei splittiä, tai etenemistä")

        return splitHappened

    def checkExplode(self, d):
        if d == 4:
            self.explode()
            return True
        if isinstance(self.left, snailfish):
             self.left.checkExplode(d+1)
        if isinstance(self.right, snailfish):
            self.right.checkExplode(d+1)
        return False

data = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
#data = [[[[4,3],4],4],[7,[[8,4],9]]]

def parseList(l):
    if isinstance(l[0], list):
        left = parseList(l[0])
    else:
        left = l[0]
    if isinstance(l[1], list):
        right = parseList(l[1])
    else:
        right = l[1]
    temp = snailfish()
    temp.set(left, right)
    temp.childParent()
    return temp

def findNextLeft(ss, s, n):
    if isinstance(s.getL(), int):
        s.left += n
    else:
        if not isinstance(s.parent, str):
            findNextLeft(s, s.parent, n)
        elif ss != s.left:
            findNextLeftU(s.left, n)

def findNextRight(ss, s, n):
    if isinstance(s.getR(), int):
        s.right += n
    else:
        if not isinstance(s.parent, str):
            findNextRight(s, s.parent, n)
        elif ss != s.right:
            findNextRightU(s.right, n)

def findNextRightU(s, n):
    if isinstance(s.getL(), int):
        s.left += n
    else:
        findNextRightU(s.left, n)

def findNextLeftU(s, n):
    if isinstance(s.getR(), int):
        s.right += n
    else:
        findNextLeftU(s.rigth, n)




#ss = parseList([[[[[9,8],1],2],3],4])
#ss.print()
#print()
#ss.reduce(0)
#ss.print()
#print()
#print("#########")

#
#ss = parseList([7,[6,[5,[4,[3,2]]]]])
#ss.print()
#print()
#ss.reduce(0)
#ss.print()
#print()
#print("#########")
#
#ss = parseList([[6,[5,[4,[3,2]]]],1])
#ss.print()
#print()
#ss.reduce(0)
#ss.print()
#print()
#print("#########")
##
#ss = parseList([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
#ss.print()
#print()
#ss.reduce(0)
#ss.print()
#print()
#print("#########")
#
#ss = parseList([[1,2],[[[[3,4],5],6],7]])
#ss.print()
#print()
#ss.reduce(0)
#ss.print()
#print()
#print("#########")
#
#ss = parseList([11,2])
#ss.print()
#print()
#ss.reduce(0)
#ss.print()
#print()
#print("#########")


file = open("test_input.txt", "r")

base = file.readline()
print(base)
so = parseList(base)
so.print()
print()
for i in range(1, len(data)):
    print(data[i])
    sf = parseList(data[i])
    tmpl = so
    so = snailfish()
    tmpl.setParent(so)
    sf.setParent(so)
    so.set(tmpl, sf)
    so.print()
    print("..")
    so.reduce(0)
    so.print()
