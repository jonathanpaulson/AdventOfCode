#!/usr/bin/python3
import sys
from collections import defaultdict, Counter

infile = sys.argv[1] if len(sys.argv)>1 else '7.in'
X = [int(x) for x in open(infile).read().strip().split(',')]

# Find [T] to minimize \sum_{x in X} |x-T|
# To find a minimum, find where the derivative is 0.
# Cost to change [T] to [T-1]? Well, cost increases by 1 for every x>=T.
# Cost decreases by 1 for every x<=T-1. So the delta is |# of X to right of T| - |# of X to left of T|.
# Increasing T by 1 is the opposite.
# So the best T has the same number of x on both sides!
# So the best T is the median!

# Find [T] to minimize \sum_{x in X} |x-T|*(|x-T|+1)/2
# (x-T)^2/2 + |x-T|/2
# (x-T)*-1 + {1 if x<T else -1}/2 = 0

X.sort()
T = X[len(X)//2]
ans = 0

def C2(d):
    # binomial coefficient (d+1 choose 2)
    # 1+2+3+...+d ~ d**2. d terms, which average (d+1)/2.
    return d*(d+1)/2

best = 1e9
for med in range(2000):
    score = 0
    for x in X:
        d = abs(x-med)
        score += C2(d)
    if score < best:
        best = score
print(best)
