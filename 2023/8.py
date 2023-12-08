import sys
import re
from math import gcd
from collections import defaultdict, Counter
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

GO = {'L': {}, 'R': {}}
steps, rule = D.split('\n\n')
for line in rule.split('\n'):
  st, lr = line.split('=')
  st = st.strip()
  left,right = lr.split(',')
  left = left.strip()[1:].strip()
  right = right[:-1].strip()
  GO['L'][st] = left
  GO['R'][st] = right

def solve(part2):
  POS = []
  for s in GO['L']:
    if s.endswith('A' if part2 else 'AAA'):
      POS.append(s)
  T = {}
  t = 0
  while True:
    NP = []
    for i,p in enumerate(POS):
      p = GO[steps[t%len(steps)]][p]
      if p.endswith('Z'):
        T[i] = t+1
        # we need to solve t % A[i] == 0 for 6 different values of A[i]
        # in general, you could have to sole t % A[i] = B[i].
        # you can do this with the chinese remainder theorem.
        if len(T) == len(POS):
          return lcm(T.values())
      NP.append(p)
    POS = NP
    #if all(p.endswith('Z') for p in POS):
    #  break
    t += 1
  assert False
print(solve(False))
print(solve(True))
