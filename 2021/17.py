#!/usr/bin/python3
import sys
import heapq
import itertools
from collections import defaultdict, Counter, deque

#target area: x=96..125, y=-144..-98

# y(t) ~ -t^2 + DY*t

p2 = 0
ans = 0
for DX in range(150):
    for DY in range(-150, 1000):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        for t in range(1000):
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            #if 20<=x<=30 and -10<=y<=-5:
            if 96<=x<=125 and -144<=y<=-98:
                ok = True
        if ok:
            p2 += 1
            if max_y > ans:
                ans = max_y
                print(DX,DY,ans)
print(ans)
print(p2)
