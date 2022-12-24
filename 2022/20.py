#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '20.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

def solve(part):
    X = [int(x) for x in lines]
    if part == 2:
        X = [x*811589153 for x in X]
    X = deque(list(enumerate(X)))
    for t in range(10 if part==2 else 1):
        for i in range(len(X)):
            for j in range(len(X)):
                if X[j][0]==i:
                    break
            while X[0][0]!=i:
                X.append(X.popleft())
            val = X.popleft()
            to_pop = val[1]
            to_pop %= len(X)
            assert 0<=to_pop < len(X)

            for _ in range(to_pop):
                X.append(X.popleft())
            X.append(val)
    for j in range(len(X)):
        if X[j][1] == 0:
            break
    return (X[(j+1000)%len(X)][1] + X[(j+2000)%len(X)][1] + X[(j+3000)%len(X)][1])
print(solve(1))
print(solve(2))
