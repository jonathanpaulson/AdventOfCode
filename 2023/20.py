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

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (ans*x)//math.gcd(x,ans)
  return ans

TYP = {}

R = {}
for line in L:
  src, dest = line.split('->')
  src = src.strip()
  dest = dest.strip()
  dest = dest.split(', ')
  R[src] = dest
  TYP[src[1:]] = src[0]

def adjust(y):
  if y in TYP:
    return TYP[y]+y
  else:
    return y

FROM = {}
INV = defaultdict(list)
for x,ys in R.items():
  R[x] = [adjust(y) for y in ys]
  for y in R[x]:
    if y[0]=='&':
      if y not in FROM:
        FROM[y] = {}
      FROM[y][x] = 'lo'
    INV[y].append(x)

assert len(INV['rx'])==1
assert INV['rx'][0][0]=='&'
WATCH = INV[INV['rx'][0]]

lo = 0 
hi = 0
Q = deque()
ON = set()
PREV = {}
COUNT = defaultdict(int)
TO_LCM = []
for t in range(1, 10**8):
  Q.append(('broadcaster', 'button', 'lo'))

  while Q:
    x, from_, typ = Q.popleft()

    if typ=='lo':
      # Assume &df -> rx AND &a -> df, &b -> df, etc.
      # We want to know when &a,&b get 'lo' input, because then they will send a 'hi' input to &df
      # When will &df get lo inputs from all of them?
      # Assume that they get lo inputs on a perfect cycle and that df must get a 'hi' input from all of them on the same
      #  timestamp. I assume they get a lot of 'hi' inputs on other timestamps that "reset" them?
      if x in PREV and COUNT[x]==2 and x in WATCH:
        #print(f't={t} cycle={t-PREV[x]} x={x} new_typ={new_typ}')
        TO_LCM.append(t-PREV[x])
      PREV[x] = t
      COUNT[x] += 1
    if len(TO_LCM) == len(WATCH):
      print(lcm(TO_LCM))
      sys.exit(0)

    if x=='rx' and typ=='lo':
      # won't happen; takes too long
      print(t+1)

    if typ=='lo':
      lo += 1
    else:
      hi += 1

    if x not in R:
      continue
    if x=='broadcaster':
      for y in R[x]:
        Q.append((y, x, typ))
    elif x[0]=='%':
      if typ=='hi':
        continue
      else:
        if x not in ON:
          ON.add(x)
          new_typ = 'hi'
        else:
          ON.discard(x)
          new_typ = 'lo'
        for y in R[x]:
          Q.append((y, x, new_typ))
    elif x[0]=='&':
      FROM[x][from_] = typ
      new_typ = ('lo' if all(y=='hi' for y in FROM[x].values()) else 'hi')
      for y in R[x]:
        Q.append((y, x, new_typ))
    else:
      assert False, x
  if t==1000:
    print(lo*hi)
