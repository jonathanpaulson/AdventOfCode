#!/usr/bin/python3
import sys
from functools import cache
from collections import defaultdict, Counter, deque
import z3

D = sys.stdin.read()
p1 = 0
p2 = 0
for line in D.splitlines():
    words = line.split()
    goal = words[0]
    goal = goal[1:-1]
    goal_n = 0
    for i,c in enumerate(goal):
        if c=='#':
            goal_n += 2**i

    buttons = words[1:-1]
    B = []
    NS = []
    for button in buttons:
        ns = [int(x) for x in button[1:-1].split(',')]
        button_n = sum(2**x for x in ns)
        B.append(button_n)
        NS.append(ns)

    score = len(buttons)
    for a in range(2**len(buttons)):
        an = 0
        a_score = 0
        for i in range(len(buttons)):
            if ((a>>i)%2) == 1:
                an ^= B[i]
                a_score += 1
        if an == goal_n:
            score = min(score, a_score)
    p1 += score

    # solve Ax = B
    # where A = effect of each button
    # x = how many times we press each button
    # B = goal state
    # minimize(sum(X))
    joltage = words[-1]
    joltage_ns = [int(x) for x in joltage[1:-1].split(',')]
    V = []
    for i in range(len(buttons)):
        V.append(z3.Int(f'B{i}'))
    EQ = []
    for i in range(len(joltage_ns)):
        terms = []
        for j in range(len(buttons)):
            if i in NS[j]:
                terms.append(V[j])
        eq = (sum(terms) == joltage_ns[i])
        EQ.append(eq)
    o = z3.Optimize()
    o.minimize(sum(V))
    for eq in EQ:
        o.add(eq)
    for v in V:
        o.add(v >= 0)
    assert o.check()
    M = o.model()
    for d in M.decls():
        #print(d.name(), M[d])
        p2 += M[d].as_long()

print(p1)
print(p2)
