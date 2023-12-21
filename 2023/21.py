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

for r in range(R):
  for c in range(C):
    if G[r][c]=='S':
      sr,sc = r,c

def findD(r,c):
  D = {}
  Q = deque([(0,0,sr,sc,0)])
  while Q:
    tr,tc,r,c,d = Q.popleft()
    if r<0:
      tr -= 1
      r += R
    if r>=R:
      tr += 1
      r -= R
    if c<0:
      tc -= 1
      c += C
    if c>=C:
      tc += 1
      c -= C
    if not (0<=r<R and 0<=c<C and G[r][c]!='#'):
      continue
    if (tr,tc,r,c) in D:
      continue
    if abs(tr)>4 or abs(tc)>4:
      continue
    D[(tr,tc,r,c)] = d
    for dr,dc in [[-1,0],[0,1],[1,0],[0,-1]]:
      Q.append((tr,tc,r+dr, c+dc, d+1))
  return D

D = findD(sr,sc)

SOLVE = {}
def solve(d,v,L):
  amt = (L-d)//R
  if (d,v,L) in SOLVE:
    return SOLVE[(d,v,L)]
  ret = 0
  for x in range(1,amt+1):
    if d+R*x<=L and (d+R*x)%2==(L%2):
      ret += ((x+1) if v==2 else 1)
  SOLVE[(d,v,L)] = ret
  #print(f'd={d} v={v} L={L} R={R} amt={amt} ret={ret}')
  return ret

def solve21(part1):
  L = (64 if part1 else 26501365)
  ans = 0
  for r in range(R):
    for c in range(C):
      if (0,0,r,c) in D:
        #print('='*20, r, c, D[(0,0,r,c)], '='*20)
        def fast(tr,tc):
          ans = 0
          B = 3
          if tr>B:
            ans += R*(abs(tr)-B)
            tr = B
          if tr<-B:
            ans += R*(abs(tr)-B)
            tr = -B
          if tc>B:
            ans += C*(abs(tc)-B)
            tc = B
          if tc<-B:
            ans += C*(abs(tc)-B)
            tc = -B
          #print(tr,tc,r,c,D[(tr,tc,r,c)])
          ans += D[(tr,tc,r,c)]
          return ans
        #for tr in range(-8,8):
        #  msg = []
        #  for tc in range(-8,8):
        #    msg.append(str(D[(tr,tc,r,c)]))
        #  #print(' '.join(msg))
        #for tr in range(-8,8):
        #  for tc in range(-8,8):
        #    assert D[(tr,tc,r,c)]==fast(tr,tc), f'{tr} {tc} {D[(tr,tc,r,c)]} {fast(tr,tc)}'

        # How many ways are there to get a copy of (r,c) in L steps?
        # interior point: just check that point
        # edge: represents everything in that direction. can add arbitrarily many R to distance
        # corner: represents everything in that quadrant. can add arbitrarily many R or C to that distance

        # CEEEC
        # E...E
        # E...E
        # E...E
        # CEEEC
        assert R==C
        OPT = [-3,-2,-1,0,1,2,3]
        for tr in OPT:
          for tc in OPT:
            if part1 and (tr!=0 or tc!=0):
              continue
            d = D[(tr,tc,r,c)]
            if d%2==L%2 and d<=L:
              ans += 1
            if tr in [min(OPT),max(OPT)] and tc in [min(OPT),max(OPT)]:
              ans += solve(d,2,L)
            elif tr in [min(OPT),max(OPT)] or tc in [min(OPT),max(OPT)]:
              ans += solve(d,1,L)
  return ans
print(solve21(True))
print(solve21(False))
