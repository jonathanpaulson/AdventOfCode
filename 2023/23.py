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

sys.setrecursionlimit(10**6)

def solve(part1):
  V = set()
  for r in range(R):
    for c in range(C):
      nbr = 0
      for ch,dr,dc in [['^',-1,0],['v', 1,0],['<', 0,-1],['>',0,1]]:
        if (0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!='#'):
          nbr += 1
      if nbr>2 and G[r][c]!='#':
        V.add((r,c))

  for c in range(C):
    if G[0][c]=='.':
      V.add((0,c))
      start = (0,c)
    if G[R-1][c]=='.':
      V.add((R-1,c))
      end = (R-1,c)

  E = {}
  for (rv,cv) in V:
    E[(rv,cv)] = []
    Q = deque([(rv,cv,0)])
    SEEN = set()
    while Q:
      r,c,d = Q.popleft()
      if (r,c) in SEEN:
        continue
      SEEN.add((r,c))
      if (r,c) in V and (r,c) != (rv,cv):
        E[(rv,cv)].append(((r,c),d))
        continue
      for ch,dr,dc in [['^',-1,0],['v', 1,0],['<', 0,-1],['>',0,1]]:
        if (0<=r+dr<R and 0<=c+dc<C and G[r+dr][c+dc]!='#'):
          if part1 and G[r][c] in ['<', '>', '^', 'v'] and G[r][c]!=ch:
            continue
          Q.append((r+dr,c+dc,d+1))

  count = 0
  ans = 0
  SEEN = [[False for _ in range(C)] for _ in range(R)]
  seen = set()
  def dfs(v,d):
    nonlocal count
    nonlocal ans
    count += 1
    r,c = v
    if SEEN[r][c]:
      return
    SEEN[r][c] = True
    if r==R-1:
      ans = max(ans, d)
    for (y,yd) in E[v]:
      dfs(y,d+yd)
    SEEN[r][c] = False
  dfs(start,0)
  #print(count)
  return ans
print(solve(True))
print(solve(False))
