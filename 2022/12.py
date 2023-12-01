#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '12.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

G = []
for line in lines:
    G.append(line)
R = len(G)
C = len(G[0])

E = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            E[r][c] = 1
        elif G[r][c] == 'E':
            E[r][c] = 26
        else:
            E[r][c] = ord(G[r][c])-ord('a')+1

def bfs(part):
    Q = deque()
    for r in range(R):
        for c in range(C):
            if (part==1 and G[r][c]=='S') or (part==2 and E[r][c] == 1):
                Q.append(((r,c), 0))

    S = set()
    while Q:
        (r,c),d = Q.popleft()
        if (r,c) in S:
            continue
        S.add((r,c))
        if G[r][c]=='E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and E[rr][cc]<=1+E[r][c]:
                Q.append(((rr,cc),d+1))
print(bfs(1))
print(bfs(2))
