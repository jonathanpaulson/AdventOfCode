import sys
from typing import List
from dataclasses import dataclass
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq

# Impose a coordinate system on the grid with grid points at the center of each square.
# We start on the square centered at (0,0). Each square corresponds to the grid point in its center.
# We are tracing out some shape by following the instructions; instead of cutting out whole squares,
# imagine drawing a line through the corresponding grid points.

# Pick's theorem: Suppose we have a polygon with integer coordinates with area A,
# B integer points along its boundary, and I integer points strictly within.
# Then A = I + (B/2) - 1.

# The solution to the problem is just I+B, the number of grid points / squares in the shape,
# plus the number of squares/points on the inside of the shape.
# Rearranging, Pick's theorem tells us I = A - (B/2) + 1.
# So I+B = A + (B/2) + 1.
# B is just the perimeter - the sum of N across all commands.
# (note: each command actually covers N+1 squares, but the ending square of each command is also covered by the
#  starting square of the next command. So summing N gets the correct number of squares in the path)
# We can compute the area A in two different ways:
# - The shoelace formula: A = (\sum X[i]*Y[i+1] - X[i+1]*Y[i]) // 2
# - Green's theorem: A = \sum y * dx = \sum x * dy

@dataclass
class Instruction:
  d: str
  n: int

def parseInput(input_: str, part2: bool) -> List[Instruction]:
  ans = []
  for line in input_.split('\n'):
    d, n, hex_ = line.split()
    if not part2:
      ans.append(Instruction(d, int(n)))
    else:
      hex_ = hex_[1:-1]
      d = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex_[-1])]
      n = int(hex_[1:-1], 16)
      ans.append(Instruction(d, n))
  return ans

def areaShoelace(cmds: List[Instruction]) -> int:
  V = []
  # x y
  pos = (0,0)
  for cmd in cmds:
    d,n = cmd.d, cmd.n
    if d == 'R':
      pos = (pos[0]+n, pos[1])
    elif d == 'D':
      pos = (pos[0], pos[1]-n)
    elif d == 'L':
      pos = (pos[0]-n, pos[1])
    elif d=='U':
      pos = (pos[0], pos[1]+n)
    V.append(pos)
  area = 0
  for i in range(len(V)):
    area -= V[i][0]*V[(i+1)%len(V)][1]
    area += V[i][1]*V[(i+1)%len(V)][0]
  area //= 2
  return area

def areaGreen(cmds: List[Instruction]) -> int:
  area = 0
  y = 0
  for cmd in cmds:
    if cmd.d=='R':
      area += y*cmd.n
    elif cmd.d=='L':
      area -= y*cmd.n
    elif cmd.d=='U':
      y += cmd.n
    elif cmd.d=='D':
      y -= cmd.n
  return area

D = open(sys.argv[1]).read().strip()
for part2 in [False,True]:
  cmds = parseInput(D,part2)
  perimeter = 0
  for cmd in cmds:
    perimeter += cmd.n
  area1 = areaShoelace(cmds)
  area2 = areaGreen(cmds)
  assert area1 == area2, f'shoelace={area1} green={area2}'
  ans = area1 + (perimeter//2) + 1
  print(ans)
