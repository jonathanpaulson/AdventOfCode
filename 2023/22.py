import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])

BS = []
for line in L:
  st,ed = line.split('~')
  sx,sy,sz = [int(x) for x in st.split(',')]
  ex,ey,ez = [int(x) for x in ed.split(',')]
  B = []
  if sx==ex and sy==ey:
    assert sz<=ez
    for z in range(sz, ez+1):
      B.append((sx,sy,z))
  elif sx==ex and sz==ez:
    assert sy<=ey
    for y in range(sy, ey+1):
      B.append((sx,y,sz))
  elif sy==ey and sz==ez:
    assert sx<=ex
    for x in range(sx, ex+1):
      B.append((x,sy,sz))
  else:
    assert False
  assert len(B)>=1
  BS.append(B)

SEEN = set()
for B in BS:
  for (x,y,z) in B:
    SEEN.add((x,y,z))

while True:
  any_ = False
  for i,B in enumerate(BS):
    ok = True
    for (x,y,z) in B:
      if z==1:
        ok = False
      if (x,y,z-1) in SEEN and (x,y,z-1) not in B:
        ok = False
    if ok:
      any_ = True
      for (x,y,z) in B:
        assert (x,y,z) in SEEN
        SEEN.discard((x,y,z))
        SEEN.add((x,y,z-1))
      BS[i] = [(x,y,z-1) for (x,y,z) in B]
  if not any_:
    break
#print(f't={t}')

# how many bricks are there s.t. no other brick would move?
from copy import deepcopy
OLD_SEEN = deepcopy(SEEN)
OLD_B = deepcopy(BS)

p1 = 0
p2 = 0
for i,B in enumerate(BS):
  SEEN = deepcopy(OLD_SEEN)
  BS = deepcopy(OLD_B)
  for C in BS:
    for (x,y,z) in C:
      assert (x,y,z) in SEEN

  for (x,y,z) in B:
    SEEN.discard((x,y,z))

  FALL = set()
  while True:
    any_ = False
    for j,C in enumerate(BS):
      if j==i:
        continue
      ok = True
      for (x,y,z) in C:
        if z==1:
          ok = False
        if (x,y,z-1) in SEEN and (x,y,z-1) not in C:
          ok = False
      if ok:
        FALL.add(j)
        for (x,y,z) in C:
          assert (x,y,z) in SEEN
          SEEN.discard((x,y,z))
          SEEN.add((x,y,z-1))
        BS[j] = [(x,y,z-1) for (x,y,z) in C]
        any_ = True
    if not any_:
      break
  if len(FALL)==0:
    p1 += 1
  p2 += len(FALL)
print(p1)
print(p2)
