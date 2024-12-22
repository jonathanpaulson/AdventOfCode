import sys
import z3
import re
import heapq
import functools
from collections import defaultdict, Counter, deque
from copy import deepcopy
from sympy.solvers.solveset import linsolve
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '22.in'
D = open(infile).read().strip()

def mix(x,y):
    return x^y
def prune(x):
    return x%16777216

def prices(x):
    ans = [x]
    for _ in range(2000):
        x = prune(mix(x, 64*x))
        x = prune(mix(x, x//32))
        x = prune(mix(x, x*2048))
        ans.append(x)
    return ans

def changes(P):
    return [P[i+1]-P[i] for i in range(len(P)-1)]

def getScores(P, C):
    ANS = {}
    for i in range(len(C)-3):
        pattern = (C[i], C[i+1], C[i+2], C[i+3])
        if pattern not in ANS:
            ANS[pattern] = P[i+4]
    return ANS

p1 = 0
SCORE = {}
for line in D.split('\n'):
    P = prices(int(line))
    p1 += P[-1]
    P = [x%10 for x in P]
    C = changes(P)
    S = getScores(P,C)
    for k,v in S.items():
        if k not in SCORE:
            SCORE[k] = v
        else:
            SCORE[k] += v
print(p1)
print(max(SCORE.values()))
