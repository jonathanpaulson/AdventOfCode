import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

def f(s):
  h = 0
  for c in s:
    h = ((h+ord(c))*17)%256
  return h

cmds = D.split(',')

p1 = 0
for cmd in cmds:
  p1 += f(cmd)
print(p1)

BOX = [[] for _ in range(256)]
for cmd in cmds:
  if cmd[-1]=='-':
    name = cmd[:-1]
    h = f(name)
    BOX[h] = [(n,v) for (n,v) in BOX[h] if n!=name]
  elif cmd[-2]=='=':
    name = cmd[:-2]
    h = f(name)
    len_ = int(cmd[-1])
    if name in [n for (n,v) in BOX[h]]:
      BOX[h] = [(n, len_ if name==n else v) for (n,v) in BOX[h]]
    else:
      BOX[h].append((name, len_))

p2 = 0
for i,box in enumerate(BOX):
  for j,(n,v) in enumerate(box):
    p2 += (i+1)*(j+1)*v
print(p2)
