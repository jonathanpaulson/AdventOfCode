import sys
import z3
import re
import heapq
from collections import defaultdict, Counter, deque
import sympy
from sympy.solvers.solveset import linsolve
import pyperclip as pc
import numpy as np
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('\d+', s)]
infile = sys.argv[1] if len(sys.argv)>=2 else '13.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()

# cost 3 to press A, 1 to press B
def solve(ax,ay,bx,by,px,py,part2):
    P2 = 10000000000000 if part2 else 0
    px += P2
    py += P2

    t1 = z3.Int('t1')
    t2 = z3.Int('t2')
    SOLVE = z3.Solver()
    SOLVE.add(t1>0)
    SOLVE.add(t2>0)
    SOLVE.add(t1*ax+t2*bx == px)
    SOLVE.add(t1*ay+t2*by == py)
    if SOLVE.check() == z3.sat:
        M = SOLVE.model()
        ret = M.eval(3*t1+t2).as_long()
        return ret
    else:
        return 0

solved = 0
machines = D.split('\n\n')
for i,machine in enumerate(machines):
    ax,ay,bx,by,px,py = ints(machine)
    p1 += solve(ax,ay,bx,by,px,py, False)
    p2 += solve(ax,ay,bx,by,px,py, True)

pr(p1)
pr(p2)
