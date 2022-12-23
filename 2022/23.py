#!/usr/bin/python3
import sys
from decimal import Decimal
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '23.in'
data = open(infile).read()
lines = [x for x in data.split('\n')]

E = set()
G = lines
for r,row in enumerate(G):
    for c,ch in enumerate(row):
        if ch=='#':
            E.add((r,c))

def show(E):
    r1 = min(r for (r,c) in E)
    r2 = max(r for (r,c) in E)
    c1 = min(c for (r,c) in E)
    c2 = max(c for (r,c) in E)
    for r in range(r1,r2+1):
        row = ''
        for c in range(c1,c2+1):
            row += ('#' if (r,c) in E else '.')
        print(row)
    print('='*80)

dir_list = ['N', 'S', 'W', 'E']
for t in range(10000):
    any_moved = False
    # P[(r,c)] is the list of elves who want to move to (r,c)
    P = defaultdict(list)
    for (r,c) in E:
        # if you don't have any neighbor, stay put
        has_nbr = False
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                if (dr!=0 or dc!=0) and (r+dr, c+dc) in E:
                    has_nbr = True
        if not has_nbr:
            continue

        moved = False
        for dir_ in dir_list:
            if dir_=='N' and (not moved) and (r-1,c) not in E and (r-1,c-1) not in E and (r-1,c+1) not in E:
                P[(r-1,c)].append((r,c))
                moved = True
            elif dir_=='S' and (not moved) and (r+1,c) not in E and (r+1, c-1) not in E and (r+1, c+1) not in E:
                P[(r+1,c)].append((r,c))
                moved = True
            elif dir_=='W' and (not moved) and (r, c-1) not in E and (r-1,c-1) not in E and (r+1,c-1) not in E:
                P[(r,c-1)].append((r,c))
                moved = True
            elif dir_=='E' and (not moved) and (r, c+1) not in E and (r-1,c+1) not in E and (r+1,c+1) not in E:
                P[(r,c+1)].append((r,c))
                moved = True

    dir_list = dir_list[1:]+[dir_list[0]]
    for k,vs in P.items():
        if len(vs) == 1:
            any_moved = True
            E.discard(vs[0])
            E.add(k)

    if not any_moved:
        print(t+1)
        break
    if t==9:
        r1 = min(r for (r,c) in E)
        r2 = max(r for (r,c) in E)
        c1 = min(c for (r,c) in E)
        c2 = max(c for (r,c) in E)
        ans = 0
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                if (r,c) not in E:
                    ans += 1
        print(ans)
