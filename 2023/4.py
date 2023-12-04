import sys
import re
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
lines = D.split('\n')
p1 = 0
N = defaultdict(int)
for i,line in enumerate(lines):
  N[i] += 1
  first, rest = line.split('|')
  id_, card = first.split(':')
  card_nums = [int(x) for x in card.split()]
  rest_nums = [int(x) for x in rest.split()]
  val = len(set(card_nums) & set(rest_nums))
  if val > 0:
    p1 += 2**(val-1)
  for j in range(val):
    N[i+1+j] += N[i]
print(p1)
print(sum(N.values()))
