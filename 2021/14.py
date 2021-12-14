#!/usr/bin/python3
import sys
import itertools
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else '14.in'

S, rules = open(infile).read().split('\n\n')

R = {}
for line in rules.strip().split('\n'):
    start,end = line.strip().split(' -> ')
    R[start] = end

# Keep track of *counts* of each pair of letters
# C1 = {pair of characters: count of that pair}
C1 = Counter()
for i in range(len(S)-1):
    C1[S[i]+S[i+1]] += 1

for t in range(41):
    if t in [10,40]:
        # CF = {character: how many times that character appears}
        CF = Counter()
        # Most letters are both the first letter *and* the second letter of a pair.
        # If we take the first letter of each pair, we count every character except the last one.
        # But the last character is the same as the last character of the original string!
        # We never add characters to the end.
        # So just add that.
        for k in C1:
            CF[k[0]] += C1[k]
        CF[S[-1]] += 1
        print(max(CF.values())-min(CF.values()))

    # If AB->R, then AB becomes (AR, RB)
    C2 = Counter()
    for k in C1:
        C2[k[0]+R[k]] += C1[k]
        C2[R[k]+k[1]] += C1[k]
    C1 = C2
