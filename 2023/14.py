import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

def rotate(G):
  R = len(G)
  C = len(G[0])
  NG = [['?' for _ in range(R)] for _ in range(C)]
  for r in range(R):
    for c in range(C):
      NG[c][R-1-r] = G[r][c]
  return NG

def roll(G):
  R = len(G)
  C = len(G[0])
  for c in range(C):
    for _ in range(R):
      for r in range(R):
        if G[r][c]=='O' and r>0 and G[r-1][c]=='.':
          G[r][c]='.'
          G[r-1][c] = 'O'
  return G

def score(G):
  ans = 0
  R = len(G)
  C = len(G[0])
  for r in range(R):
    for c in range(C):
      if G[r][c]=='O':
        ans += len(G)-r
  return ans

def show(G):
  for r in range(len(G)):
    print(''.join(G[r]))


BY_GRID = {}

target = 10**9
t = 0
while t<target:
  t += 1
  for j in range(4):
    G = roll(G)
    if t==1 and j==0:
      print(score(G)) # part1
    G = rotate(G)
  #print('='*80)
  #show(G)
  #print('='*80)
  Gh = tuple(tuple(row) for row in G)
  if Gh in BY_GRID:
    cycle_length = t-BY_GRID[Gh]
    amt = (target-t)//cycle_length
    t += amt * cycle_length
  BY_GRID[Gh] = t
print(score(G))
