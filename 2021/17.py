#!/usr/bin/python3
import sys
import heapq
import itertools
from collections import defaultdict, Counter, deque
from math import ceil, sqrt

#target area: x=20..30, y=-10..-5
# MinX, MaxX = (20, 30)
# MinY, MaxY = (-10, -5)

#target area: x=96..125, y=-144..-98
MinX, MaxX = (96, 125)
MinY, MaxY = (-144, -98)

# y(t) ~ -t^2 + DY*t

p2 = 0
ans = 0

minDX = int(ceil((sqrt(8*MinX+1)-1)/2))
for DX in range(minDX, MaxX+1):
    for DY in range(MinY, -MinY):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        while x <= MaxX and y >= MinY:
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1

            if MinX <= x <= MaxX and MinY <= y <= MaxY:
                ok = True
                break
        if ok:
            p2 += 1
            if max_y > ans:
                ans = max_y
                print(DX,DY,ans)
print(ans)
print(p2)
