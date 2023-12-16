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

DR = [-1,0,1,0]
DC = [0,1,0,-1]
def step(r,c,d):
  return (r+DR[d], c+DC[d], d)

def score(sr,sc,sd):
  POS = [(sr,sc,sd)]
  SEEN = set()
  SEEN2 = set()
  while True:
    NP = []
    if not POS:
      break
    for (r,c,d) in POS:
      #print(r,c,d)
      if 0<=r<R and 0<=c<C:
        SEEN.add((r,c))
        if (r,c,d) in SEEN2:
          continue
        SEEN2.add((r,c,d))
        ch = G[r][c]
        if ch=='.':
          NP.append(step(r,c,d))
        elif ch=='/':
          # up right down left
          NP.append(step(r,c,{0:1, 1:0, 2:3, 3:2}[d]))
        elif ch=='\\':
          NP.append(step(r,c,{0:3, 1:2, 2:1, 3:0}[d]))
        elif ch=='|':
          if d in [0,2]:
            NP.append(step(r,c,d))
          else:
            NP.append(step(r, c, 0))
            NP.append(step(r, c, 2))
        elif ch=='-':
          if d in [1,3]:
            NP.append(step(r,c,d))
          else:
            NP.append(step(r, c, 1))
            NP.append(step(r, c, 3))
        else:
          assert False
    POS = NP
  return len(SEEN)

print(score(0,0,1))
ans = 0
for r in range(R):
  ans = max(ans, score(r,0,1))
  ans = max(ans, score(r,C-1,3))
for c in range(C):
  ans = max(ans, score(0,c,2))
  ans = max(ans, score(R-1,c,0))
print(ans)
