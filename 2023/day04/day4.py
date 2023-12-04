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
ans, cardAns, wins = 0, 0, 0
cards = []
for i in range(1, len(data)+1):
    cards.append(1)

for d in data:
    card = int(d.split(":")[0].split()[1])
    ownNumbers = d.split(":")[1].strip().split("|")[0].strip().split()
    winNumbers = d.split(":")[1].strip().split("|")[1].strip().split()
    #print(card)
    #print(ownNumbers)
    #print(winNumbers)
    #print("Card: ", card)
    for o in ownNumbers:
        if o in winNumbers:
            if cardAns == 0:
                cardAns = 1
            else:
                cardAns *= 2
            wins += 1

    for i in range(0, wins):
        cards[card+i] += cards[card-1]
        #print(cards)
    wins = 0
    ans += cardAns
    cardAns = 0

print("Part1: ", ans)
print("Part2: ", sum(cards))
