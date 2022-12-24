#!/usr/bin/python3
import sys
from decimal import Decimal
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '24.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

G = lines
R = len(G)
C = len(G[0])
#print(G,R,C)

r = 0
c = 0
while G[r][c]=='#':
  c += 1 

BAD_CELLS = {}
for t in range((R-2)*(C-2)+1):
  BAD = set()
  for rr in range(R):
    for cc in range(C):
      if G[rr][cc]=='>':
        BAD.add((rr, 1+((cc-1+t)%(C-2))))
      elif G[rr][cc]=='v':
        BAD.add((1+((rr-1+t)%(R-2)), cc))
      elif G[rr][cc]=='<':
        BAD.add((rr, 1+((cc-1-t)%(C-2))))
      elif G[rr][cc]=='^':
        BAD.add((1+((rr-1-t)%(R-2)), cc))
        assert 0<=(rr-1-t)%(R-2)<R-2
      if cc == c:
        assert G[rr][cc] != '^' and G[rr][cc]!='v'
      if cc == C-2:
        assert G[rr][cc]!='^' and G[rr][cc]!='v'
  BAD_CELLS[t] = BAD

p1 = False
SEEN = set()
start = (r,c,0,False,False)
Q = deque([start])
while Q:
  (r,c,t,got_end,got_start) = Q.popleft()
  if not (0<=r<R and 0<=c<C and G[r][c]!='#'):
    continue
  if r==R-1 and got_end and got_start:
    print(t)
    break
  if r==R-1 and (not p1):
    print(t)
    p1 = True
  if r==R-1:
    got_end = True
  if r==0 and got_end:
    got_start = True
  #t %= ((R-2)*(C-2))
  if(r,c,t,got_start,got_end) in SEEN:
    continue
  SEEN.add((r,c,t,got_start,got_end))
  BAD = BAD_CELLS[t+1]

  if (r,c) not in BAD:
    Q.append((r,c,t+1,got_end,got_start))
  if (r+1,c) not in BAD:
    Q.append((r+1, c, t+1,got_end,got_start))
  if (r-1,c) not in BAD:
    Q.append((r-1, c, t+1,got_end,got_start))
  if (r,c+1) not in BAD:
    Q.append((r, c+1, t+1,got_end,got_start))
  if (r,c-1) not in BAD:
    Q.append((r, c-1, t+1,got_end,got_start))
