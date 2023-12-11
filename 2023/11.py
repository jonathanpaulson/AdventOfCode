import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])
for r in range(R):
  assert len(G[r])==C

EMPTY_R = []
r = 0
while r<R:
  empty = True
  for c in range(C):
    if G[r][c] == '#':
      empty = False
  if empty:
    EMPTY_R.append(r)
    #print('EMPTY R', r)
    #G = G[:r]+[G[r]]+G[r:]
    #R += 1
    #assert len(G)==R
    #r += 1
  r += 1
EMPTY_C = []
c = 0
while c<C:
  empty = True
  for r in range(R):
    if G[r][c]=='#':
      empty = False
  if empty:
    EMPTY_C.append(c)
    #for r in range(R):
    #  G[r] = G[r][:c]+[G[r][c]]+G[r][c:]
    #C += 1
    #c += 1
  c += 1

GAL = []
for r in range(R):
  for c in range(C):
    if G[r][c]=='#':
      GAL.append((r,c))

for part2 in [False,True]:
  expansion_factor = 10**6-1 if part2 else 2-1
  ans = 0
  for i,(r,c) in enumerate(GAL):
    for j in range(i,len(GAL)):
      r2,c2 = GAL[j]
      dij = abs(r2-r)+abs(c2-c)
      for er in EMPTY_R:
        if min(r,r2)<=er<=max(r,r2):
          dij += expansion_factor
      for ec in EMPTY_C:
        if min(c,c2)<=ec<=max(c,c2):
          dij += expansion_factor
      #print(i+1,j+1,dij,(r,c),(r2,c2))
      ans += dij
  print(ans)
