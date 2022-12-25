#!/usr/bin/python3
import sys
from decimal import Decimal
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '25.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

def to_base10(s):
  ans = 0
  base = 1
  for i,d in enumerate(reversed(s)):
    vd = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[d]
    ans += vd*base
    base *= 5
  return ans

def max_value(p5):
  if p5==1:
    return 2
  return p5*2 + max_value(p5//5)

def to_snafu(n,p5):
  D = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}
  if -2 <= n <= 2:
    return D[n]
  assert abs(n)<=max_value(p5)
  for d in [-2,-1,0,1,2]:
    nn = n-p5*d
    if abs(nn)<=max_value(p5//5):
      return D[d]+to_snafu(n-p5*d, p5//5)
  assert False, (n, p5,n//p5)

ans = 0
for line in lines:
  ans += to_base10(line)
p5 = 1
while abs(ans)>max_value(p5):
  p5 *= 5
print(to_snafu(ans,p5))

max_len = 0
for line in lines:
  max_len = max(max_len, len(line))

VD = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
D = {2: '2', 1: '1', 0: '0', -1: '-', -2:'='}
ans = ''
carry = 0
for i in range(max_len):
  sum_i = carry
  for line in lines:
    if i<len(line):
      sum_i += VD[line[i]]
  carry = 0
  while sum_i >= 3:
    carry += 1
    sum_i -= 3
  while sum_i <= -3:
    carry -= 1
    sum_i += 3
  assert -2<=sum_i<=2
  ans += D[sum_i]
  #print(i,D[sum_i])
#print(''.join(list(reversed(ans))))
