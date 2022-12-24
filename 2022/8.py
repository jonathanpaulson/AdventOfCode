#!/usr/bin/python3
import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv)>1 else '8.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

G = []
for line in lines:
    row = line
    G.append(row)

DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(G)
C = len(G[0])

p1 = 0
for r in range(R):
    for c in range(C):
        vis = False
        for (dr,dc) in DIR:
            rr = r
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if G[rr][cc] >= G[r][c]:
                    ok = False
            if ok:
                vis = True
        if vis:
            p1 += 1
print(p1)

p2 = 0
for r in range(R):
    for c in range(C):
        score = 1
        for (dr,dc) in DIR:
            dist = 1
            rr = r+dr
            cc = c+dc
            while True:
                if not (0<=rr<R and 0<=cc<C):
                    dist -= 1
                    break
                if G[rr][cc]>=G[r][c]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        p2 = max(p2, score)
print(p2)


