#!/usr/bin/python3
import sys
import itertools
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else '11.in'

G = []
for line in open(infile):
    G.append([int(x) for x in line.strip()])


R = len(G)
C = len(G[0])

ans = 0
def flash(r,c):
    global ans
    ans += 1
    G[r][c] = -1
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and G[rr][cc]!=-1:
                G[rr][cc] += 1
                if G[rr][cc] >= 10:
                    flash(rr,cc)

t = 0
while True:
    t += 1
    for r in range(R):
        for c in range(C):
            G[r][c] += 1
    for r in range(R):
        for c in range(C):
            if G[r][c] == 10:
                flash(r,c)
    done = True
    for r in range(R):
        for c in range(C):
            if G[r][c] == -1:
                G[r][c] = 0
            else:
                done = False
    if t == 100:
        print(ans)
    if done:
        print(t)
        break
