#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else '18.in'
data = open(infile).read().strip()


ans = None

def add(n1, n2):
  ret = [n1, n2]
  return reduce_(ret)

def reduce_(n):
  did1, n1 = explode(n)
  if did1:
    return reduce_(n1)
  else:
    did2, n2 = split(n)
    if did2:
      return reduce_(n2)
    else:
      return n2
 
def explode(n):
  ns = str(n)
  nums = re.findall('\d+', ns)
  parts = []
  i = 0
  while i < len(ns):
    if ns[i] == '[':
      parts.append('[')
      i += 1
    elif ns[i] == ',':
      parts.append(',')
      i += 1
    elif ns[i] == ']':
      parts.append(']')
      i += 1
    elif ns[i] == ' ':
      i += 1
    else:
      assert ns[i].isdigit()
      j = i
      while j < len(ns) and ns[j].isdigit():
        j += 1
      parts.append(int(ns[i:j]))
      i = j

  depth = 0
  for i,c in enumerate(parts):
    if c=='[':
      depth += 1
      if depth == 5:
        old_ns = ns
        left = parts[i+1]
        assert isinstance(left, int)
        assert parts[i+2] == ','
        right = parts[i+3]
        assert isinstance(right, int)
        left_i = None
        right_i = None
        for j in range(len(parts)):
          if isinstance(parts[j], int) and j < i:
            left_i = j
          elif isinstance(parts[j], int) and j>i+3 and right_i is None:
            right_i = j
        if right_i is not None:
          assert right_i > i
          parts[right_i] += right
        parts = parts[:i] + [0] + parts[i+5:]
        if left_i is not None:
          parts[left_i] += left
        return True, ast.literal_eval(''.join([str(x) for x in parts]))
    elif c==']':
      depth -= 1
    else:
      pass
  return False, n

def split(n):
  if isinstance(n, list):
    did1, n1 = split(n[0])
    if did1:
      return True, [n1, n[1]]
    else:
      did2, n2 = split(n[1])
      return did2, [n1, n2]
  else:
    assert isinstance(n, int)
    if n >= 10:
      return True, [n//2, (n+1)//2]
    else:
      return False, n

def magnitude(n):
  if isinstance(n, list):
    return 3*magnitude(n[0]) + 2*magnitude(n[1])
  else:
    return n
  

X = []
for line in data.split('\n'):
  assert line == line.strip()
  X.append(ast.literal_eval(line))

ans = None
for x in X:
  for y in X:
    if x != y:
      score = magnitude(add(x, y))
      if ans is None or score > ans:
        ans = score
print(ans)
