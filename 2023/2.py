import sys
from collections import defaultdict
D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0
#only 12 red cubes, 13 green cubes, and 14 blue cubes?
for line in D.split('\n'):
  ok = True
  id_, line = line.split(':')
  V = defaultdict(int)
  for event in line.split(';'):
    for balls in event.split(','):
      n,color = balls.split()
      n = int(n)
      V[color] = max(V[color], n)
      if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
        ok = False
  score = 1
  for v in V.values():
    score *= v
  p2 += score
  if ok:
    p1 += int(id_.split()[-1])
print(p1)
print(p2)
