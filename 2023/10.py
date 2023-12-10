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

# find coordinates of S and replace with correct type of pipe
for r in range(R):
  for c in range(C):
    if G[r][c]=='S':
      sr,sc = r,c
      up_valid = (G[r-1][c] in ['|','7','F'])
      right_valid = (G[r][c+1] in ['-','7','J'])
      down_valid = (G[r+1][c] in ['|','L','J'])
      left_valid = (G[r][c-1] in ['-','L','F'])
      assert sum([up_valid, right_valid, down_valid, left_valid]) == 2
      if up_valid and down_valid:
        G[r][c]='|'
        sd = 0
      elif up_valid and right_valid:
        G[r][c]='L'
        sd = 0
      elif up_valid and left_valid:
        G[r][c]='J'
        sd = 0
      elif down_valid and right_valid:
        G[r][c]='F'
        sd = 2
      elif down_valid and left_valid:
        G[r][c]='7'
        sd = 2
      elif left_valid and right_valid:
        G[r][c]='-'
        sd = 1
      else:
        assert False

# up right down left
DR = [-1,0,1,0]
DC = [0,1,0,-1]
r = sr
c = sc
d = sd
dist = 0
while True:
  dist += 1
  r += DR[d]
  c += DC[d]
  if G[r][c]=='L':
    if d not in [2,3]:
      break
    elif d==2:
      d = 1
    else:
      d = 0
  if G[r][c]=='J':
    if d not in [1,2]:
      break
    elif d==1:
      d = 0
    else:
      d = 3
  if G[r][c]=='7':
    # up right down left
    if d not in [0,1]:
      break
    elif d==0:
      d = 3
    else:
      d = 2
  if G[r][c]=='F':
    if d not in [0,3]:
      break
    elif d==0:
      d = 1
    else:
      d = 2
  assert G[r][c] != '.'
  if (r,c) == (sr,sc):
    print(dist//2)
    break

# replace every square with 3x3 of ground/wall e.g.
#      .x.
# | -> .x.
#      .x.
R2 = 3*R
C2 = 3*C
G2 = [['.' for _ in range(C2)] for _ in range(R2)]
for r in range(R):
  for c in range(C):
    if G[r][c]=='|':
      G2[3*r+0][3*c+1] = 'x'
      G2[3*r+1][3*c+1] = 'x'
      G2[3*r+2][3*c+1] = 'x'
    elif G[r][c]=='-':
      G2[3*r+1][3*c+0] = 'x'
      G2[3*r+1][3*c+1] = 'x'
      G2[3*r+1][3*c+2] = 'x'
    elif G[r][c]=='7':
      G2[3*r+1][3*c+0] = 'x'
      G2[3*r+1][3*c+1] = 'x'
      G2[3*r+2][3*c+1] = 'x'
    elif G[r][c]=='F':
      G2[3*r+2][3*c+1] = 'x'
      G2[3*r+1][3*c+1] = 'x'
      G2[3*r+1][3*c+2] = 'x'
    elif G[r][c]=='J':
      G2[3*r+1][3*c+0] = 'x'
      G2[3*r+1][3*c+1] = 'x'
      G2[3*r+0][3*c+1] = 'x'
    elif G[r][c]=='L':
      G2[3*r+0][3*c+1] = 'x'
      G2[3*r+1][3*c+1] = 'x'
      G2[3*r+1][3*c+2] = 'x'
    elif G[r][c]=='.':
      pass
    else:
      assert False, G[r][c]
for row in G2:
  #print(''.join(row))
  pass

Q = deque()
SEEN = set()
# up right down left
for r in range(R2):
  Q.append((r,0))
  Q.append((r,C2-1))
for c in range(C2):
  Q.append((0,c))
  Q.append((R2-1,c))
while Q:
  # either (r,c) for ground or (r,c,in_or_out) for pipe
  r,c = Q.popleft()
  if (r,c) in SEEN:
    continue
  if not (0<=r<R2 and 0<=c<C2):
    continue
  #print(r,c,G[r//3][c//3])
  SEEN.add((r,c))
  if G2[r][c]=='x':
    continue
  for d in range(4):
    Q.append((r+DR[d],c+DC[d]))
ans = 0
for r in range(R):
  for c in range(C):
    seen = False
    for rr in [0,1,2]:
      for cc in [0,1,2]:
        if (3*r+rr,3*c+cc) in SEEN:
          seen = True
    if not seen:
      ans += 1
print(ans)
