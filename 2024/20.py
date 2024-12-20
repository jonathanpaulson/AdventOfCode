import sys
import z3
import re
import heapq
import functools
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

infile = sys.argv[1] if len(sys.argv)>=2 else '20.in'
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

DIST = {}
Q = deque([(0,er,ec)])
while Q:
    d,r,c = Q.popleft()
    if (r,c) in DIST:
        continue
    DIST[(r,c)] = d
    for dr,dc in DIRS:
        rr,cc = r+dr, c+dc
        if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
            Q.append((d+1,rr,cc))

def find_cheat(d0, CHEAT_TIME):
    ans = set()
    Q = deque([(0,None,None,None,sr,sc)])
    SEEN = set()
    SAVE = 100
    while Q:
        d,cheat_start,cheat_end,cheat_time,r,c = Q.popleft()
        assert cheat_end is None
        if d>=d0-SAVE:
            continue
        if G[r][c] == 'E':
            if cheat_end is None:
                cheat_end = (r,c)
            if d<=d0-SAVE and (cheat_start,cheat_end) not in ans:
                #print(d,d0,r,c,cheat_start,cheat_end,cheat_time)
                ans.add((cheat_start, cheat_end))
        if (r,c,cheat_start,cheat_end,cheat_time) in SEEN:
            continue
        SEEN.add((r,c,cheat_start,cheat_end,cheat_time))
        #if len(SEEN) % 1000000 == 0:
        #    print(len(SEEN))

        if cheat_start is None: # start cheat
            assert G[r][c] != '#'
            Q.append((d,(r,c),None,CHEAT_TIME,r,c))
        if cheat_time is not None and G[r][c]!='#': # and cheat_time==0: # end cheat
            assert G[r][c] in ['.', 'S', 'E']
            if DIST[(r,c)] <= d0-100-d:
                ans.add((cheat_start, (r,c)))
                #if len(ans) % 1000 == 0:
                #    print(len(ans), d+DIST[(r,c)])
            #Q.append((d,cheat_start,(r,c),None,r,c))
        if cheat_time == 0:
            continue
        else:
            for dr,dc in DIRS:
                rr,cc = r+dr, c+dc
                if cheat_time is not None:
                    assert cheat_time > 0
                    if 0<=rr<R and 0<=cc<C:
                        Q.append((d+1,cheat_start,None,cheat_time-1,rr,cc))
                else:
                    if 0<=rr<R and 0<=cc<C and G[rr][cc]!='#':
                        Q.append((d+1,cheat_start,cheat_end,cheat_time,rr,cc))
    #print(len(SEEN))
    return len(ans)

d0 = DIST[(sr,sc)]
print(find_cheat(d0, 2))
print(find_cheat(d0, 20))
