import sys
import z3
import re
import heapq
from collections import defaultdict, Counter, deque
from sympy.solvers.solveset import linsolve
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '16.in'
ans = 0
D = open(infile).read().strip()

G = D.split('\n')
R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            sr,sc = r,c
        if G[r][c] == 'E':
            er,ec = r,c

Q = []
SEEN = set()
heapq.heappush(Q, (0,sr,sc,1))
DIST = {}
best = None
while Q:
    d,r,c,dir = heapq.heappop(Q)
    if (r,c,dir) not in DIST:
        DIST[(r,c,dir)] = d
    if r==er and c==ec and best is None:
        best = d
    if (r,c,dir) in SEEN:
        continue
    SEEN.add((r,c,dir))
    dr,dc = DIRS[dir]
    rr,cc = r+dr,c+dc
    if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
        heapq.heappush(Q, (d+1, rr,cc,dir))
    heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
    heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))
print(best)

Q = []
SEEN = set()
for dir in range(4):
    heapq.heappush(Q, (0,er,ec,dir))
DIST2 = {}
while Q:
    d,r,c,dir = heapq.heappop(Q)
    if (r,c,dir) not in DIST2:
        DIST2[(r,c,dir)] = d
    if (r,c,dir) in SEEN:
        continue
    SEEN.add((r,c,dir))
    # going backwards instead of forwards here
    dr,dc = DIRS[(dir+2)%4]
    rr,cc = r+dr,c+dc
    if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
        heapq.heappush(Q, (d+1, rr,cc,dir))
    heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
    heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))

OK = set()
for r in range(R):
    for c in range(C):
        for dir in range(4):
            # (r,c,dir) is on an optimal path if the distance from start to end equals the distance from start to (r,c,dir) plus the distance from (r,c,dir) to end.
            if (r,c,dir) in DIST and (r,c,dir) in DIST2 and DIST[(r,c,dir)] + DIST2[(r,c,dir)] == best:
                OK.add((r,c))
print(len(OK))
