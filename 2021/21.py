#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque
from aocd import submit

infile = sys.argv[1] if len(sys.argv)>1 else '21.in'
data = open(infile).read().strip()

p1 = 7-1
p2 = 2-1
#p1 = 4-1
#p2 = 8-1
die = 0

def roll():
  global die
  die += 1
  return die

s1 = 0
s2 = 0
while True:
  m1 = roll() + roll() + roll()
  p1 = (p1 + m1) % 10
  s1 += p1+1
  if s1 >= 1000:
    print(s2*die)
    break

  m2 = roll() + roll() + roll()
  p2 = (p2+m2)%10
  s2 += p2+1
  if s2 >= 1000:
    print(s1*die)
    break

# dynamic programming!
# brute force + memoization.
# how many possible game states are there?
# 10 options for p1, 10 options for p2, 21 options for s1, 21 options for s2 -> 10*10*21*21 ~ 40,000
# total running time ~ state space * non-recursive time for one call ~ 40e3 * 27 ~ 120e4 = ~1M
p1 = 7-1
p2 = 2-1
DP = {} # game state -> answer for that game state
def count_win(p1, p2, s1, s2):
  # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
  # return (# of universes where player A wins, # of universes where player B wins)
  if s1 >= 21:
    return (1,0)
  if s2 >= 21:
    return (0, 1)
  if (p1, p2, s1, s2) in DP:
    return DP[(p1, p2, s1, s2)]
  ans = (0,0)
  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_p1 = (p1+d1+d2+d3)%10
        new_s1 = s1 + new_p1 + 1

        x1, y1 = count_win(p2, new_p1, s2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)
  DP[(p1, p2, s1, s2)] = ans
  return ans

print(max(count_win(p1, p2, 0, 0)))
