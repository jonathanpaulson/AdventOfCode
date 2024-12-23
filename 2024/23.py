import sys
import z3
import re
import heapq
import functools
from collections import defaultdict, Counter, deque
from copy import deepcopy
from sympy.solvers.solveset import linsolve
import random
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '23.in'
D = open(infile).read().strip()

E = defaultdict(set)
for line in D.split('\n'):
    a,b, = line.split('-')
    E[a].add(b)
    E[b].add(a)

xs = sorted(E.keys())

p1 = 0
for i,a in enumerate(xs):
    for j in range(i+1, len(xs)):
        for k in range(j+1, len(xs)):
            b = xs[j]
            c = xs[k]
            if a in E[b] and a in E[c] and b in E[c]:
                if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                    p1 += 1
pr(p1)

best = None
for t in range(1000):
    random.shuffle(xs)
    clique = []
    for x in xs:
        ok = True
        for y in clique:
            if x not in E[y]:
                ok = False
        if ok:
            clique.append(x)
    if best is None or len(clique) > len(best):
        best = clique
        #print(t, len(best), ','.join(sorted(best)))
pr(','.join(sorted(best)))
