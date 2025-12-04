#!/usr/bin/python3
import sys
from collections import defaultdict, Counter

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])

p1 = 0
p2 = 0
first = True
while True:
    changed = False
    for r in range(R):
        for c in range(C):
            nbr = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    rr,cc = r+dr,c+dc
                    if 0<=rr<R and 0<=cc<C and G[rr][cc]=='@':
                        nbr += 1
            if G[r][c]=='@' and nbr<5:
                p1 += 1
                changed = True
                if not first:
                    p2 += 1
                    G[r][c]='.'
    if first:
        print(p1)
        first = False
    if not changed:
        break

print(p2)
