import sys
import re
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
ans = 0 

t,d = L
times = [int(x) for x in t.split(':')[1].split()]
dist = [int(x) for x in d.split(':')[1].split()]

T = ''
for t in times:
  T += str(t)
T = int(T)
D = ''
for d in dist:
  D += str(d)
D = int(D)

def f(t, d):
  # runs in O(log(t))
  # let g(x) = x*(t-x) is maximized at t//2
  # we want to know: what is the lowest value s.t. g(x) >= d
  # we want to know: what is the highest value s.t. g(x) >= d
  def g(x):
    return x*(t-x)
  lo = 0
  hi = t//2
  if hi*(t-hi) < d:
    return 0
  assert g(lo)<d and g(hi)>=d
  while lo+1<hi:
    m = (lo+hi)//2
    if g(m)>=d:
      hi = m
    else:
      lo = m
  assert lo+1 == hi
  assert g(lo)<d and g(hi)>=d
  first = hi
  assert g(first)>=d and g(first-1)<d

  # g(x) == g(t-x), so there's symmetry about the midpoint t/2
  last = int((t/2) + (t/2-first))
  assert g(last)>=d and g(last+1)<d, f'last={last} g(last)={g(last)} {g(last+1)} d={d}'
  return last-first+1

ans = 1
for i in range(len(times)):
  ans *= f(times[i], dist[i])
print(ans)
print(f(T,D))
