import sys
import re
import heapq
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else '11.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()
D = [int(x) for x in D.split()]

DP = {}
def solve(x, t):
    """If we put [x] through [t] steps, how long is the resulting list?"""
    if (x,t) in DP:
        return DP[(x,t)]
    if t==0:
        ret = 1
    elif x==0:
        ret = solve(1, t-1)
    elif len(str(x))%2==0:
        dstr = str(x)
        left = dstr[:len(dstr)//2]
        right = dstr[len(dstr)//2:]
        left, right = (int(left), int(right))
        ret = solve(left, t-1) + solve(right, t-1)
    else:
        ret = solve(x*2024, t-1)
    DP[(x,t)] = ret
    return ret

def solve_all(t):
    return sum(solve(x, t) for x in D)
pr(solve_all(25))
pr(solve_all(75))
