#!/usr/bin/python3
import sys
import itertools
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else '9.in'
G = []
for line in open(infile):
    G.append([int(x) for x in list(line.strip())])
R = len(G)
C = len(G[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]
ans = 0
for r in range(R):
    assert len(G[r])==C
    for c in range(C):
        ok = True
        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            if 0<=rr<R and 0<=cc<C and G[rr][cc]<=G[r][c]:
                ok = False
        if ok:
            ans += G[r][c]+1
print(ans)

S = []
SEEN = set()
for r in range(R):
    for c in range(C):
        if (r,c) not in SEEN and G[r][c]!=9:
            size = 0
            Q = deque()
            Q.append((r,c))
            while Q:
                (r,c) = Q.popleft()
                if (r,c) in SEEN:
                    continue
                SEEN.add((r,c))
                size += 1
                for d in range(4):
                    rr = r+DR[d]
                    cc = c+DC[d]
                    if 0<=rr<R and 0<=cc<C and G[rr][cc]!=9:
                        Q.append((rr,cc))
            S.append(size)
S.sort()
print(S[-1]*S[-2]*S[-3])



