#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque
from aocd import submit

#submit(len(G), part="a", day=20, year=2021)
infile = sys.argv[1] if len(sys.argv)>1 else '22.in'
data = open(infile).read().strip()

# [1 10] [11 20] [21 100]
X = set()
Y = set()
Z = set()
C = []
min_x = 0
min_y = 0
min_z = 0
max_x = 0
max_y = 0
max_z = 0
G = set()
for r,line in enumerate(data.strip().split('\n')):
  assert line == line.strip()
  words = line.split()
  cmd = words[0]
  x1,x2,y1,y2,z1,z2 = [int(x) for x in re.findall('-?\d+', words[1])]
  x1,x2 = min(x1, x2), max(x1,x2)
  y1,y2 = min(y1, y2), max(y1,y2)
  z1,z2 = min(z1, z2), max(z1,z2)

  X.add(x1)
  X.add(x2+1)
  Y.add(y1)
  Y.add(y2+1)
  Z.add(z1)
  Z.add(z2+1)

  min_x = min(x1, min_x)
  min_y = min(y1, min_y)
  min_z = min(z1, min_z)
  max_x = max(x2, max_x)
  max_y = max(y2, max_y)
  max_z = max(z2, max_z)
  C.append((x1,x2,y1,y2,z1,z2,cmd=='on'))

def expand(A):
  B = set()
  for x in A:
    B.add(x)
  B = sorted(B)

  ret = {}
  U = {}
  len_sum = 0
  for i,x in enumerate(B):
    ret[x] = i
    if i+1 < len(B):
      len_ = B[i+1]-x if i+1<len(B) else None
      len_sum += len_
      U[i] = len_
  for a in A:
    assert a in ret
  assert len_sum == max(B)-min(B), f'{len_sum} {max(B)-min(B)}'
  return (ret, U)

X.add(-50)
X.add(51)
Y.add(-50)
Y.add(51)
Z.add(-50)
Z.add(51)

X,UX = expand(X)
Y,UY = expand(Y)
Z,UZ = expand(Z)

#print(len(X), len(Y), len(Z))

def solve(p1):
  G = set()
  for t,(x1,x2,y1,y2,z1,z2,on) in enumerate(C):
    #print(t,len(C))
    if p1:
      x1 = max(x1, -50)
      y1 = max(y1, -50)
      z1 = max(z1, -50)
      
      x2 = min(x2, 50)
      y2 = min(y2, 50)
      z2 = min(z2, 50)
    for x in range(X[x1], X[x2+1]):
      for y in range(Y[y1], Y[y2+1]):
        for z in range(Z[z1], Z[z2+1]):
          #print(x,y,z,UX[x],UY[y],UZ[z])
          if on:
            G.add((x,y,z))
          else:
            G.discard((x,y,z))

  ans = 0
  for x,y,z in G:
    lx = UX[x]
    ly = UY[y]
    lz = UZ[z]
    ans += lx*ly*lz
  return ans

print(solve(True))
print(solve(False))
