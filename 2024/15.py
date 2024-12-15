import sys
import z3
import re
import heapq
from collections import defaultdict, Counter, deque
from sympy.solvers.solveset import linsolve
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '15.in'
D = open(infile).read().strip()

G, instrs = D.split('\n\n')
G = G.split('\n')

def solve(G,part2):
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]
    if part2:
        BIG_G = []
        for r in range(R):
            row = []
            for c in range(C):
                if G[r][c]=='#':
                    row.append('#')
                    row.append('#')
                if G[r][c]=='O':
                    row.append('[')
                    row.append(']')
                if G[r][c]=='.':
                    row.append('.')
                    row.append('.')
                if G[r][c]=='@':
                    row.append('@')
                    row.append('.')
            BIG_G.append(row)
        G = BIG_G
        C *= 2

    for r in range(R):
        for c in range(C):
            if G[r][c] == '@':
                sr,sc = r,c
                G[r][c] = '.'

    r,c = sr,sc
    for inst in instrs:
        if inst == '\n':
            continue
        dr,dc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[inst]
        #print(r,c,inst)
        rr,cc = r+dr,c+dc
        if G[rr][cc]=='#':
            continue
        elif G[rr][cc]=='.':
            r,c = rr,cc
        elif G[rr][cc] in ['[', ']', 'O']:
            Q = deque([(r,c)])
            SEEN = set()
            ok = True
            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                rrr,ccc = rr+dr, cc+dc
                if G[rrr][ccc]=='#':
                    ok = False
                    break
                if G[rrr][ccc] == 'O':
                    Q.append((rrr,ccc))
                if G[rrr][ccc]=='[':
                    Q.append((rrr,ccc))
                    assert G[rrr][ccc+1]==']'
                    Q.append((rrr,ccc+1))
                if G[rrr][ccc]==']':
                    Q.append((rrr,ccc))
                    assert G[rrr][ccc-1]=='['
                    Q.append((rrr,ccc-1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for rr,cc in sorted(SEEN):
                    rrr,ccc = rr+dr,cc+dc
                    if (rrr,ccc) not in SEEN:
                        assert G[rrr][ccc] == '.'
                        G[rrr][ccc] = G[rr][cc]
                        G[rr][cc] = '.'
                        SEEN.remove((rr,cc))
            r = r+dr
            c = c+dc

    #for r in range(R):
    #    print(''.join(G[r]))
    ans = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] in ['[', 'O']:
                ans += 100*r+c
    return ans
pr(solve(G, False))
pr(solve(G, True))
