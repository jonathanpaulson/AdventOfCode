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

infile = sys.argv[1] if len(sys.argv)>=2 else '18.in'
ans = 0
D = open(infile).read().strip()

N = 71
G = [['.' for c in range(N)] for r in range(N)]
for i,line in enumerate(D.split('\n')):
    x,y = [int(x) for x in line.split(',')]
    if 0<=y<N and 0<=x<N:
        G[y][x] = '#'

    Q = deque([(0,0,0)])
    SEEN = set()
    ok = False
    while Q:
        d,r,c = Q.popleft()
        if (r,c) == (N-1,N-1):
            if i==1023:
                pr(d)
            ok = True
            break
        if (r,c) in SEEN:
            continue
        SEEN.add((r,c))
        for dr,dc in DIRS:
            rr = r+dr
            cc = c+dc
            if 0<=rr<N and 0<=cc<N and G[rr][cc] != '#':
                Q.append((d+1,rr,cc))
    if not ok:
        pr(f'{x},{y}')
        break
