#!/usr/bin/env python3
import sys
import math
import time
from functools import cache
sys.setrecursionlimit(20000)

input_file = "test.txt"
input_file = 'input.txt'

ans = 0

if len(sys.argv) >  1 :
    input_file = sys.argv[1]

with open(input_file) as f:
    data = f.readlines()

data = [d.strip() for d in data]

@cache
def arrangements(row, numbers):
    #print(row, numbers)
    if len(numbers) == 0:
        return 1 if "#" not in row else 0
    if len(row) == 0:
        return 1 if len(numbers) == 0 else 0

    curc = row[0]
    curn = int(numbers.split(",")[0])
    answer = 0

    if curc in "?.":
        answer += arrangements(row[1:], numbers)
    # eka on tai voi olla #
    if curc in "#?":
        legal = True
        # tarkistetaan voiko tulla laillinen jos #
        if len(row) < curn:
            legal = False
        if "." in row[:curn]:
            legal = False
        if len(row) > curn and row[curn] == "#":
            legal = False

        if legal and "," in numbers:
            answer += arrangements(row[curn+1:], numbers[numbers.index(",")+1:])
        elif len(row) > curn and "#" in row[curn+1:]:
            legal = False
        elif legal:
                answer += 1

    return answer

start = time.perf_counter()
tans = 0

#print(dd)
#
testi = ".##?#????????????????? 4,14"
#data = [testi]
for dd in data:
    tans = 0
    row = dd.split(" ")
    nums = row[1]
    row = row[0]
    #nums = eval(nums)
    #ans += count_arrangements(row, nums)
    ans += arrangements(row, nums)

end = time.perf_counter()
print("part1:", ans)
print("aikaa meni:",  end-start)

start = time.perf_counter()
ans = 0

#print(dd)
for dd in data:
    tans = 0
    row = dd.split(" ")
    nums = row[1]
    row = row[0]
    row = "?".join([row] * 5)
    nums = ",".join([nums] * 5)
    ans += arrangements(row, nums)

end = time.perf_counter()
print("part2:", ans)
print("aikaa meni:",  end-start)
