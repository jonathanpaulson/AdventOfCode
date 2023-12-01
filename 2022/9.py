#!/usr/bin/python3
import sys
from collections import defaultdict
infile = sys.argv[1] if len(sys.argv)>1 else '9.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

def adjust(H,T):
    dr = (H[0]-T[0])
    dc = (H[1]-T[1])
    if abs(dr)<=1 and abs(dc)<=1:
        # ok
        pass
    elif abs(dr)>=2 and abs(dc)>=2:
        #2       2       2 
        # 1   ->  1   ->  .   -> 2
        #  H       .H      1H     1H
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(dr)>=2:
        # T     T       .
        #  H ->  .H  ->  TH
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(dc)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T

H = (0,0)
T = [(0,0) for _ in range(9)]
DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
P1 = set([T[0]])
P2 = set([T[8]])
for line in lines:
    d,amt = line.split()
    amt = int(amt)
    for _ in range(amt):
        H = (H[0] + DR[d], H[1]+DC[d])
        T[0] = adjust(H, T[0])
        for i in range(1, 9):
            T[i] = adjust(T[i-1], T[i])
        P1.add(T[0])
        P2.add(T[8])
print(len(P1))
print(len(P2))
