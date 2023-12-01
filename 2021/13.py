#!/usr/bin/python3
import sys
import itertools
from collections import defaultdict, Counter, deque

infile = sys.argv[1] if len(sys.argv)>1 else '13.in'

did_p1 = False
G = {}
for line in open(infile):
    line = line.strip()
    if line and line.startswith('fold'):
        G2 = {}
        instr = line.split()[-1]
        d,v = instr.split('=')
        v = int(v)
        if d == 'x':
            for (x,y) in G:
                if x < v:
                    G2[(x,y)] = True
                else:
                    G2[(v-(x-v), y)] = True
        else:
            assert d == 'y'
            for (x,y) in G:
                if y < v:
                    G2[(x,y)] = True
                else:
                    G2[(x, v-(y-v))] = True
        G = G2
        if not did_p1:
            did_p1 = True
            print(len(G2))
    elif line:
        x,y = [int(v) for v in line.strip().split(',')]
        G[(x,y)] = True

X = max([x for x,y in G.keys()])
Y = max([y for x,y in G.keys()])

ans = ''
for y in range(Y+1):
    for x in range(X+1):
        ans += ('x' if (x,y) in G else ' ')
    print(ans)
    ans = ''
