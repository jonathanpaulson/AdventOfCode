#!/usr/bin/python3
import sys
from functools import cache
from collections import defaultdict, Counter, deque
import z3

D = sys.stdin.read()
parts = D.split('\n\n')
presents = parts[:-1]
SIZES = {}
for present in presents:
    lines = present.splitlines()
    name = int(lines[0][:-1])
    G = [list(row) for row in lines[1:]]
    size = 0
    for row in G:
        for c in row:
            if c=='#':
                size += 1
    SIZES[name] = size

ans = 0
regions = parts[-1]
for region in regions.splitlines():
    sz, ns = region.split(': ')
    R,C = [int(x) for x in sz.split('x')]
    ns = [int(x) for x in ns.split()]
    total_present_size = sum(n*SIZES[i] for i,n in enumerate(ns))
    total_grid_size = R*C
    print(f'{total_grid_size=} {total_present_size=}')
    if total_present_size * 1.3 < total_grid_size:
        ans += 1
    elif total_present_size > total_grid_size:
        pass
    else:
        print(f'HARD {total_grid_size=} {total_present_size=}')

print(ans)
