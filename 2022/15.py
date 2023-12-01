#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '15.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

S = set()
B = set()
sum_d = 0
for line in lines:
    words = line.split()
    sx,sy = words[2],words[3]
    bx,by = words[8],words[9]
    sx = int(sx[2:-1])
    sy = int(sy[2:-1])
    bx = int(bx[2:-1])
    by = int(by[2:])
    d = abs(sx-bx) + abs(sy-by)
    sum_d += d
    S.add((sx,sy,d))
    B.add((bx,by))

def valid(x,y,S):
    for (sx,sy,d) in S:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy<=d:
            return False
    return True

p1 = 0
for x in range(-int(1e7),int(1e7)):
    y = int(2e6)
    if not valid(x,y,S) and (x,y) not in B:
        p1 += 1
print(p1)

n_checked = 0
# If there is only one possible position for another beacon, it *must* be distance d+1 from some beacon
# If not, we could find an adjacent position that is possible.
found_p2 = False
for (sx,sy,d) in S:
    # check all points that are d+1 away from (sx,sy)
    for dx in range(d+2):
        dy = (d+1)-dx
        for signx,signy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            n_checked += 1
            x = sx+(dx*signx)
            y = sy+(dy*signy)
            if not(0<=x<=4000000 and 0<=y<=4000000):
                continue
            assert abs(x-sx)+abs(y-sy)==d+1
            if valid(x,y,S) and (not found_p2):
                print(x*4000000 + y)
                found_p2 = True
#print(n_checked, 4*sum_d) # these are approximately equal
