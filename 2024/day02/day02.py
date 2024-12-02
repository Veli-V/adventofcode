#!/usr/bin/env python3
import sys

input_file = 'input.txt'
#input_file = 'test.txt'

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

#print(data)

ok = True
ans = 0
ok2 = True
ans2 = 0

#Part1
for d in data:
    ok = True
    d = d.split()
    d = [int(a) for a in d]
    #print(d)

    if sorted(d) != d and sorted(d, reverse=True) != d:
        print(d)
        print("ei oo jarjestyksessa, abort")
        ok = False
    else:
        for i in range(len(d)-1):
            if (abs(int(d[i]) - int(d[i+1])) > 3 or int(d[i]) == int(d[i+1])):
                print(d)
                print("Ei oo ok, liian iso ero: ", d[i], d[i+1])
                ok = False
                break
    if ok:
        ans += 1
        ans2 += 1
    else:
        for j in range(len(d)):
            ok2 = True
            dd = d.copy()
            del dd[j]
            print(dd)
            if sorted(dd) != dd and sorted(dd, reverse=True) != dd:
                print(dd)
                print("ei oo jarjestyksessa, abort")
                ok2 = False
            else:
                for i in range(len(dd)-1):
                    if (abs(int(dd[i]) - int(dd[i+1])) > 3 or int(dd[i]) == int(dd[i+1])):
                        print(dd)
                        print("Ei oo ok, liian iso ero: ", dd[i], dd[i+1])
                        ok2 = False
                        break
            if ok2:
                ans2 += 1
                break


print("Part1: ", ans)
print("Part2: ", ans2)
