#!/usr/bin/env python3
import sys

input_file = "test.txt"
input_file = 'input.txt'
#input_file = "test2.txt"

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

times = data[0].split(":")[1].split()
distances = data[1].split(":")[1].split()
times = [int(t) for t in times]
distances = [int(d) for d in distances]
print(times)
print(distances)

def amountOfWins(time, distance):
    mid = int(time/2)
    check = mid
    wins, tempD = 0, 0

    while True:
        tmpD = (time - check)*check
        if tmpD > distance:
            wins += 1
        else:
            break
        check += 1
    check = mid -1
    while True:
        tmpD = (time - check)*check
        if tmpD > distance:
            wins += 1
        else:
            break
        check -= 1
    return wins


#Part1
ans = 1
tmp = 0
for idx, time in enumerate(times):
    tmp = amountOfWins(time, distances[idx])
    print("For race ", idx, " wins ", tmp)
    ans *= tmp

print("Part1: ", ans)

#part2


times = data[0].split(":")[1].replace(" ", "")
distances = data[1].split(":")[1].replace(" ", "")
times = int(times)
distances = int(distances)

ans = amountOfWins(times, distances)
print("part2: ", ans)
