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

infile = sys.argv[1] if len(sys.argv)>=2 else '25.in'
D = open(infile).read().strip()

shapes = D.split('\n\n')
keys = []
locks = []
for shape in shapes:
    G = shape.split('\n')
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]
    is_key = True
    for c in range(C):
        if G[0][c] == '#':
            is_key = False
    if is_key:
        keys.append(shape)
    else:
        locks.append(shape)

def fits(key, lock):
    R = len(key)
    assert R == len(lock)
    C = len(key[0])
    assert C == len(lock[0])
    for r in range(R):
        for c in range(C):
            if key[r][c]=='#' and lock[r][c]=='#':
                return False
    return True

ans = 0
for key in keys:
    for lock in locks:
        if fits(key, lock):
            ans += 1
pr(ans)
