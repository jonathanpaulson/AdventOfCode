#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '14.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

R = set()
for line in lines:
    prev = None
    for point in line.split('->'):
        x,y = point.split(',')
        x,y = int(x),int(y)
        if prev is not None:
            dx = x-prev[0]
            dy = y-prev[1]
            len_ = max(abs(dx),abs(dy))
            for i in range(len_+1):
                xx = prev[0]+i*(1 if dx>0 else (-1 if dx<0 else 0))
                yy = prev[1]+i*(1 if dy>0 else (-1 if dy<0 else 0))
                R.add((xx,yy))
        prev = (x,y)

floor = 2+max(r[1] for r in R)
#print(floor)
lo_x = min(r[0] for r in R)-2000
hi_x = max(r[0] for r in R)+2000
for x in range(lo_x, hi_x):
    R.add((x,floor))

did_p1 = False
for t in range(1000000):
    rock = (500,0)
    while True:
        if rock[1]+1>=floor and (not did_p1):
            did_p1 = True
            print(t)
        if (rock[0],rock[1]+1) not in R:
            rock = (rock[0],rock[1]+1)
        elif (rock[0]-1,rock[1]+1) not in R:
            rock = (rock[0]-1, rock[1]+1)
        elif (rock[0]+1, rock[1]+1) not in R:
            rock = (rock[0]+1, rock[1]+1)
        else:
            break
    if rock == (500,0):
        print(t+1)
        break
    R.add(rock)
