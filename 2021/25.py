#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque
from aocd import submit
from copy import deepcopy

#submit(len(G), part="a", day=25, year=2021)
infile = sys.argv[1] if len(sys.argv)>1 else '25.in'
data = open(infile).read().strip()

G = []
for line in data.split('\n'):
  assert line.strip() == line
  G.append(line)
R = len(G)
C = len(G[0])

t = 0
while True:
  t += 1
  moved = False
  G2 = [[G[r][c] for c in range(C)] for r in range(R)]
  for r in range(R):
    for c in range(C):
      if G[r][c] == '>':
        if G[r][(c+1)%C] == '.':
          moved = True
          G2[r][(c+1)%C] = '>'
          G2[r][c] = '.'
  G3 = [[G2[r][c] for c in range(C)] for r in range(R)]
  for r in range(R):
    for c in range(C):
      if G2[r][c] == 'v' and G2[(r+1)%R][c] == '.':
        moved = True
        G3[(r+1)%R][c] = 'v'
        G3[r][c] = '.'
  if not moved:
    print(t)
    sys.exit(0)
  G = G3
  #print(t, moved)
  #for r in range(R):
  #  row = ''
  #  for c in range(C):
  #    row += G[r][c]
  #  print(row)



