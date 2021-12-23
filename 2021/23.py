#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque
from aocd import submit
from copy import deepcopy

#submit(len(G), part="a", day=23, year=2021)
#infile = sys.argv[1] if len(sys.argv)>1 else '23.in'
#data = open(infile).read().strip()

#############
#...........#
###B#C#A#D###
  #D#C#B#A#
  #D#B#A#C#
  #B#C#D#A#
  #########
A = ['B', 'D', 'D', 'B']
B = ['C', 'C', 'B', 'C']
C = ['A', 'B', 'A', 'D']
D = ['D' ,'A', 'C', 'A']

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
#A = ['B', 'D', 'D', 'A']
#B = ['C', 'C', 'B', 'D']
#C = ['B', 'B', 'A', 'C']
#D = ['D', 'A', 'C', 'A']

TOP = []
while len(TOP) < 11:
  TOP.append('E')
start = ({'A': A, 'B': B, 'C': C, 'D': D}, TOP)

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
def done(state):
  bot, top = state
  for k,v in bot.items():
    for vv in v:
      if vv!=k:
        return False
  return True

def can_move_from(k, col):
  for c in col:
    if c!=k and c!='E':
      return True
  return False

def can_move_to(k,col):
  for c in col:
    if c!=k and c!='E':
      return False
  return True

def bot_idx(bot):
  return {'A': 2, 'B': 4, 'C': 6, 'D': 8}[bot]

def top_idx(col):
  for i,c in enumerate(col):
    if c!='E':
      return i
  return None

def dest_idx(col):
  for i,c in reversed(list(enumerate(col))):
    if c=='E':
      return i
  return None

def between(a, bot, top):
  # 0 1 A 3 B 5 C 7 D 9 10
  return (bot_idx(bot)<a<top) or (top<a<bot_idx(bot))
assert between(1, 'A', 0)

def clear_path(bot, top_idx, top):
  for ti in range(len(top)):
    if between(ti, bot, top_idx) and top[ti]!='E':
      return False
  return True

def show(state):
  bot, top = state
  C = Counter()
  for c in top:
    C[c] += 1
  for k,v in bot.items():
    for c in v:
      C[c] += 1
  assert C['A'] == 4
  assert C['B'] == 4
  assert C['C'] == 4
  assert C['D'] == 4
  assert C['E'] == 11
  assert top[2] == 'E'
  assert top[4] == 'E'
  assert top[6] == 'E'
  assert top[8] == 'E'

DP = {}
def f(state):
  # given a state, what is the cost to get to "done"?
  show(state)
  # move top -> L or R
  # move L or R -> 
  # always move to destination ASAP
  bot, top = state
  key = (tuple((k, tuple(v)) for k,v in bot.items()), tuple(top))
  if done(state):
    return 0
  if key in DP:
    return DP[key]
  # move to dest if possible
  for i,c in enumerate(top):
    if c in bot and can_move_to(c,bot[c]):
      if clear_path(c, i, top):
        di = dest_idx(bot[c])
        assert di is not None
        dist = di + 1 + abs(bot_idx(c)-i)
        cost = COST[c] * dist
        new_top = list(top)
        new_top[i] = 'E'
        top[i] = 'E'
        new_bot = deepcopy(bot)
        new_bot[c][di] = c
        #print(f'Moved top={i} c={c} dest={di}')
        return cost + f((new_bot, new_top))

  ans = int(1e9)
  for k,col in bot.items():
    if not can_move_from(k, col):
      continue
    ki = top_idx(col)
    if ki is None:
      continue
    c = col[ki]
    for to_ in range(len(top)):
      if to_ in [2, 4, 6, 8]:
        continue
      if top[to_] != 'E':
        continue
      if clear_path(k, to_, top):
        dist = ki + 1 + abs(to_ - bot_idx(k))
        new_top = list(top)
        assert new_top[to_] == 'E'
        new_top[to_] = c
        new_bot = deepcopy(bot)
        assert new_bot[k][ki] == c
        new_bot[k][ki] = 'E'
        #print(f'Moved col={k} idx={ki} c={c} to {to_}')
        ans = min(ans, COST[c]*dist + f((new_bot, new_top)))
  DP[key] = ans
  #print(len(DP), ans)
  return ans

print(f(start))
