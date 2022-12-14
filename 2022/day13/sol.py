#!/usr/bin/env python3
import sys
import ast
import inspect

input_file = 'test_input.txt'
#input_file = 'test.txt'
input_file = 'input.txt'


if len(sys.argv) >  1 :
    input_file = sys.argv[1]

data.clear()
with open(input_file) as f:
    line = f.readline().strip()
    while line:
        data.append(line)
        line = f.readline().strip()
        data.append(line)
        line = f.readline().strip()
        line = f.readline().strip()

data = [ast.literal_eval(d) for d in data]

def dprint(str):
    if input_file != 'input.txt':
        print(str)

def compare(l, r):
    if l == r: return None
    if type(l) == int and type(r) == int: return l < r
    if type(l) != list: l = [l]
    if type(r) != list: r = [r]
    for i in range(len(l)):
        if i >= len(r): return False
        left = l[i]
        right = r[i]
        ok = compare(left, right)
        if ok != None: return ok
    if len(l) < len(r): return True


oks = []

pos2, pos6 = 1,2

for i in range(1, len(data), 2):
    ok = None
    left = data[i-1]
    right = data[i]
    if compare(left, right):
        oks.append((i+1)/2)
    if compare(left, [[2]]): pos2 += 1
    if compare(right, [[2]]): pos2 += 1
    if compare(left, [[6]]): pos6 += 1
    if compare(right, [[6]]): pos6 += 1



print("Part1")
print("Sum of pairs in right order: {}".format(sum(oks)))

print("Part2:")
print("Pos for [[2]] is {} and [[6]] {} so {}".format(pos2, pos6, pos2*pos6))
