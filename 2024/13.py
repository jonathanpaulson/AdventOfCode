import sys
import re
import heapq
from collections import defaultdict, Counter, deque
import pyperclip as pc
import numpy as np
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
infile = sys.argv[1] if len(sys.argv)>=2 else '13.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()

# cost 3 to press A, 1 to press B
def solve(ax,ay,bx,by,px,py,part2):
    P2 = 10000000000000 if part2 else 0
    #A = [[ax,bx],[ay,by]]
    #B = [px+P2, py+P2]
    #x = np.linalg.solve(A,B)
    #t1 = int(x[0])
    #t2 = int(x[1])
    #print(ax*t1 + bx*t2 - (px+P2))
    #print(ay*t1 + by*t2 - (py+P2))
    #print(A,B,x)
    #assert False
    #return 3*t1 + t2
    best = None
    for t1 in range(600):
        for t2 in range(600):
            cost = 3*t1 + t2
            dx = ax*t1 + bx*t2
            dy = ay*t1 + by*t2
            if dx==dy and dx>0:
                score = dx/cost
                if best is None or score < best[0]:
                    best = (score, t1, t2, cost, dx)
    if best is None:
        return 0
    _score, t1, t2, cost, dx = best
    amt = (P2 - 40000) // dx

    DP = {}
    def f(x,y):
        """What is the minimum cost of getting to (x,y)?"""
        if (x,y) in DP:
            return DP[(x,y)]
        if x==0 and y==0:
            return 0
        if x<0:
            return 10**20
        if y<0:
            return 10**20
        ans = min(3+f(x-ax,y-ay), 1+f(x-bx,y-by))
        DP[(x,y)] = ans
        return ans
    ans = f(px + P2 - amt*dx, py + P2 - amt*dx)
    if ans < 10**15:
        return ans + amt*cost
    else:
        return 0

solved = 0
machines = D.split('\n\n')
for i,machine in enumerate(machines):
    a,b,prize = machine.split('\n')
    #['Button', 'A:', 'X+49,', 'Y+27']
    aw = a.split()
    ax = int(aw[2].split('+')[1].split(',')[0])
    ay = int(aw[3].split('+')[1].split(',')[0])
    bw = b.split()
    bx = int(bw[2].split('+')[1].split(',')[0])
    by = int(bw[3].split('+')[1].split(',')[0])
    pw = prize.split()
    px = int(pw[1].split('=')[1].split(',')[0])
    py = int(pw[2].split('=')[1])
    p1 += solve(ax,ay,bx,by,px,py, False)
    p2 += solve(ax,ay,bx,by,px,py, True)
    #print(i, len(machines), prize, p1, p2)

pr(p1)
pr(p2)
