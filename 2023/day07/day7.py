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
print(data)

cardValue = {'A': 14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.rate = self.getRate()

    def __lt__(self, other):
        sv, ov = 0, 0
        if self.rate == other.rate:
            for idx, c in enumerate(self.cards):
                sv = cardValue[c]
                ov = cardValue[other.cards[idx]]
                if sv < ov:
                    return True
                if ov < sv:
                    return False
            return False
        return self.rate < other.rate

    def __repr__(self):
        return "Cards: " + self.cards + " Rate: " + str(self.rate) + " bid: " + str(self.bid)


    def getRate(self):
        tmp = {'A': 0, 'K':0, 'Q':0, 'J':0, 'T':0, '9':0, '8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0}
        for c in self.cards:
            tmp[c] += 1
        maxSames = max(tmp.values())
        if maxSames > 3:
            return maxSames + 2
        if 3 in tmp.values() and 2 in tmp.values():
            return 5
        if 3 in tmp.values():
            return 4
        if len([i for i in tmp if tmp[i] == 2]) > 1:
            return 3
        if 2 in tmp.values():
            return 2
        else:
            return 1
        return 0

hands = []
for d in data:
    hands.append(Hand(d.split()[0], int(d.split()[1])))

hands.sort()

ans = 0
for idx, h in enumerate(hands):
    ans += (idx+1)*h.bid

print("part1:" + str(ans))
