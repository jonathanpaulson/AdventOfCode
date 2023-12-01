#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '18.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

P = set()
for line in lines:
    x,y,z = line.split(',')
    x,y,z = int(x),int(y),int(z)
    P.add((x,y,z))

OUT = set()
IN = set()
def reaches_outside(x,y,z,part):
    if (x,y,z) in OUT:
        return True
    if (x,y,z) in IN:
        return False
    SEEN = set()
    Q = deque([(x,y,z)])
    while Q:
        x,y,z = Q.popleft()
        if (x,y,z) in P:
            continue
        if (x,y,z) in SEEN:
            continue
        SEEN.add((x,y,z))
        if len(SEEN) > (5000 if part==2 else 0):
            for p in SEEN:
                OUT.add(p)
            return True
        Q.append((x+1,y,z))
        Q.append((x-1,y,z))
        Q.append((x,y+1,z))
        Q.append((x,y-1,z))
        Q.append((x,y,z+1))
        Q.append((x,y,z-1))
    for p in SEEN:
        IN.add(p)
    return False

def solve(part):
    OUT.clear()
    IN.clear()
    ans = 0
    for (x,y,z) in P:
        if reaches_outside(x+1,y,z,part):
            ans += 1
        if reaches_outside(x-1,y,z,part):
            ans += 1
        if reaches_outside(x,y+1,z,part):
            ans += 1
        if reaches_outside(x,y-1,z,part):
            ans += 1
        if reaches_outside(x,y,z+1,part):
            ans += 1
        if reaches_outside(x,y,z-1,part):
            ans += 1
    return ans
print(solve(1))
print(solve(2))
