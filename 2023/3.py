import sys
import re
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')
G = [[c for c in line] for line in lines]
R = len(G)
C = len(G[0])

p1 = 0
nums = defaultdict(list)
for r in range(len(G)):
  gears = set() # positions of '*' characters next to the current number
  n = 0
  has_part = False
  for c in range(len(G[r])+1):
    if c<C and G[r][c].isdigit():
      n = n*10+int(G[r][c])
      for rr in [-1,0,1]:
        for cc in [-1,0,1]:
          if 0<=r+rr<R and 0<=c+cc<C:
            ch = G[r+rr][c+cc]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+rr, c+cc))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        p1 += n
      n = 0
      has_part = False
      gears = set()

print(p1)
p2 = 0
for k,v in nums.items():
  if len(v)==2:
    p2 += v[0]*v[1]
print(p2)
