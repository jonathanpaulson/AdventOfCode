#!/usr/bin/python3
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else '20.in'
data = open(infile).read().strip()

rule, start = data.split('\n\n')
rule = rule.strip()
assert len(rule) == 512
#print(rule[0], rule[511])

G = set()
for r,line in enumerate(start.strip().split('\n')):
  for c,x in enumerate(line.strip()):
    if x=='#':
      G.add((r,c))

# on=true means G says what pixels are on (all the rest are off).
# on=false means G says what pixels are *off* (all the rest are on)
def step(G, on):
  G2 = set()
  rlo = min([r for r,c in G])
  rhi = max([r for r,c in G])
  clo = min([c for r,c in G])
  chi = max([c for r,c in G])
  for r in range(rlo-5, rhi+10):
    for c in range(clo-5, chi+10):
      rc_str = 0
      bit = 8
      for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
          if ((r+dr,c+dc) in G) == on:
            rc_str += 2**bit
          bit -= 1
      assert 0<=rc_str < 512
      if (rule[rc_str] == '#') != on:
        G2.add((r,c))
  return G2

def show(G):
  rlo = min([r for r,c in G])
  rhi = max([r for r,c in G])
  clo = min([c for r,c in G])
  chi = max([c for r,c in G])
  for r in range(rlo-5, rhi+5):
    row = ''
    for c in range(clo-5, chi+5):
      if (r,c) in G:
        row += '#'
      else:
        row += ' '
    print(row)
  
for t in range(50):
  if t==2:
    print(len(G))
  G = step(G, t%2==0)
print(len(G))
