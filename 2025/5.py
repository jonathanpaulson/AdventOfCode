#!/usr/bin/python3
import sys
from collections import defaultdict, Counter

D = sys.stdin.read()
ranges, ingredients = D.split('\n\n')
R = []
for r in ranges.splitlines():
    st,ed = r.split('-')
    st = int(st)
    ed = int(ed)
    R.append((st,ed))

p2 = 0
R = sorted(R)
current = -1
# |------|
#    |--------|
#     |--|

for (s,e) in R:
    if current >= s:
        s = current+1
    if s<=e:
        p2 += e-s+1
    current = max(current,e)

p1 = 0
for x in ingredients.splitlines():
    x = int(x)
    fresh = False
    for (s,e) in R:
        if s<=x<=e:
            fresh = True
    if fresh:
        p1 += 1

print(p1)
print(p2)
