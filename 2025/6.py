#!/usr/bin/python3
import sys
from collections import defaultdict, Counter

D = sys.stdin.read()
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])

p1 = 0
p2 = 0
start_c = 0
for cc in range(C+1):
    is_blank = True
    if cc<C:
        for r in range(R):
            if G[r][cc]!=' ':
                is_blank = False
    if is_blank:
        # solve problem
        op = G[R-1][start_c]
        assert op in ['+', '*'], op

        p1_score = 0 if op=='+' else 1
        for r in range(R-1):
            p1_n = 0
            for c in range(start_c, cc):
                if G[r][c]!=' ':
                    p1_n = p1_n*10 + int(G[r][c])
            if op == '*':
                p1_score *= p1_n
            else:
                p1_score += p1_n
        p1 += p1_score

        score = 0 if op=='+' else 1
        for c in range(cc-1, start_c-1, -1):
            n = 0
            for r in range(R-1):
                if G[r][c]!=' ':
                    n = n*10 + int(G[r][c])
            if op=='+':
                score += n
            else:
                score *= n
            #print(f'{c=} {n=} {op=} {score=}')
        p2 += score
        start_c = cc+1
print(p1)
print(p2)
