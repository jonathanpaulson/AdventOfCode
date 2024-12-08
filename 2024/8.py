import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else '8.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()
G = D.split('\n')
R = len(G)
C = len(G[0])
P = defaultdict(list)
for r in range(R):
    for c in range(C):
        if G[r][c] != '.':
            P[G[r][c]].append((r,c))

A1 = set()
A2 = set()
for r in range(R):
    for c in range(C):
        for k,vs in P.items():
            for (r1,c1) in vs:
                for (r2,c2) in vs:
                    if (r1,c1) != (r2,c2):
                            d1 = abs(r-r1)+abs(c-c1)
                            d2 = abs(r-r2)+abs(c-c2)

                            dr1 = r-r1
                            dr2 = r-r2
                            dc1 = c-c1
                            dc2 = c-c2
                            # To check if (r,c) (r1,c1) (r2,c2) are all on a line, check if (r,c)-(r1,c1) has the same slope as (r,c)-(r2,c2)
                            # dr1/dc1 == dr2/dc2

                            if (d1==2*d2 or d1*2==d2) and 0<=r<R and 0<=c<C and (dr1*dc2 == dc1*dr2):
                                A1.add((r,c))
                            if 0<=r<R and 0<=c<C and (dr1*dc2 == dc1*dr2):
                                #print(f'{r4=} {c=} {r1=} {c1=} {r2=} {c2=} {k=} {dr1=} {dr2=} {dc1=} {dc2=}')
                                A2.add((r,c))


p1 = len(A1)
p2 = len(A2)
pr(p1)
pr(p2)
