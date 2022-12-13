#!/usr/bin/env python3
import sys
import ast

input_file = 'test_input.txt'
#input_file = 'input.txt'


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


def compare(l, r):
    if type(l) == int and type(r) == int:
        if l < r:
            print("28: Comp {} and {} True".format(l, r))
            return True
        elif r < l:
            print("31: Comp {} and {} False".format(l, r))
            return False
    if type(l) == list and type(r) == list:
        for i in range(len(l)):
            print(l[i])
            if i >= len(r):
                print("36: Comp {} and {} False".format(l, r))
                return False
            if compare(l[i], r[i]) == False:
                print("39: Comp {} and {} False".format(l, r))
                return False
            if compare(l[i], r[i]) == True:
                print("42: Comp {} and {} True".format(l, r))
                return True
        if len(l) < len(r):
            print("45: Comp {} and {} True".format(l, r))
            return True
        print("47: Comp {} and {} None".format(l, r))
        return None
    elif type(l) == list or type(r) == list:
        if type(l) != list: l = [l]
        if type(r) != list: r = [r]
        for i in range(len(l)):
            if i >= len(r):
                print("51: Comp {} and {} False".format(l, r))
                return False
            if compare(l[i], r[i]) == False :
                print("54: Comp {} and {} False".format(l, r))
                return False
            if compare(l[i], r[i]) == True:
                print("57: Comp {} and {} True".format(l, r))
                return True
        if len(l) < len(r):
            print("63: Comp {} and {} True".format(l, r))
            return True
        print("65: Comp {} and {} None".format(l, r))
        return None
    else: return None


oks = []

for i in range(1, len(data), 2):
    ok = True
    left = data[i-1]
    right = data[i]
    print()
    print("== PAIR {} ==".format((i+1)/2))
    print()
    print("Comparing:")
    print(left)
    print(right)
    for j in range(len(left)):
        if j >= len(right):
            #print("Ei oo oikein!!!")
            break

        ok = compare(left[j], right[j])
        if ok == False:
            print("Ei oo oikein!!!")
            ok = False
            break
        elif ok == True:
            print("On oikein")
            break
    if ok: oks.append((i+1)/2)


print("Ok parit: {}, summa {}".format(oks, sum(oks)))
print(sum(oks))
