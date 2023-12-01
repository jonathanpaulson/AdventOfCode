#!/usr/bin/python3
import sys
from decimal import Decimal
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '22.in'
data = open(infile).read()
lines = [x for x in data.split('\n')]

G, instr = data.split('\n\n')
G = G.split('\n')
instr = instr.strip()

D = [(-1,0),(0,1),(1,0),(0,-1)]

R = len(G)
C = len(G[0])
for r in range(R):
    while len(G[r]) < C:
        G[r] += ' '
    assert len(G[r])==C

CUBE = C//3
assert CUBE == R//4
#print(CUBE)

# .12
# .3.
# 54.
# 6..
REGION = [(0,1),(0,2),(1,1),(2,1),(2,0),(3,0)]

def regionToGlobal(r,c,region):
    rr,cc = REGION[region-1]
    return (rr*CUBE+r,cc*CUBE+c)

def getRegion(r,c):
    for i,(rr,cc) in enumerate(REGION):
        if rr*CUBE<=r<(rr+1)*CUBE and cc*CUBE<=c<(cc+1)*CUBE:
            return (i+1, r-rr*CUBE, c-cc*CUBE)
    assert False, (r,c)

def newCoords(r,c,d,nd):
    if d==0:
        assert r==0
        x = c
    if d==1:
        assert c==CUBE-1
        x = r
    if d==2:
        assert r==CUBE-1
        x = CUBE-1-c
    if d==3:
        assert c==0
        x = CUBE-1-r

    if nd==0:
        return (CUBE-1,x)
    if nd==1:
        return (x,0)
    if nd==2:
        return (0,CUBE-1-x)
    if nd==3:
        return (CUBE-1-x,CUBE-1)

#  3   6
# 542 512
#  6   3

#  1   5
# 532 164
#  4   2

#  3   3
# 124 154
#  6   6

def getDest(r,c,d,part):
    if part == 1:
        r = (r+D[d][0])%R
        c = (c+D[d][1])%C
        while G[r][c]==' ':
            r = (r+D[d][0])%R
            c =(c+D[d][1])%C
        return (r,c,d)

    region,rr,rc = getRegion(r,c)
    # 0=up, 1=right,2=down,3=left
    # If I am leaving region R in direction D, I enter region NR in direction ND
    newRegion,nd = {
        (4,0):(3,0), (4,1):(2,3), (4,2):(6,3), (4,3):(5,3),
        (1,0):(6,1), (1,1):(2,1), (1,2):(3,2), (1,3):(5,1),
        (3,0):(1,0), (3,1):(2,0), (3,2):(4,2), (3,3):(5,2),
        (6,0):(5,0), (6,1):(4,0), (6,2):(2,2), (6,3):(1,2),
        (2,0):(6,0), (2,1):(4,3), (2,2):(3,3), (2,3):(1,3),
        (5,0):(3,1), (5,1):(4,1), (5,2):(6,2), (5,3):(1,1)}[(region,d)]

    nr,nc = newCoords(rr,rc,d,nd)
    assert 0<=nr<CUBE and 0<=nc<CUBE
    nr,nc = regionToGlobal(nr,nc,newRegion)
    assert G[nr][nc] in ['.','#'], f'{G[nr][nc]}'
    return (nr,nc,nd)

def solve(part):
    # compute starting location
    r = 0
    c = 0
    d = 1
    while G[r][c] != '.':
        c += 1

    i = 0
    while i < len(instr):
        n = 0
        while i<len(instr) and instr[i].isdigit():
            n = n*10 + int(instr[i])
            i += 1
        for _ in range(n):
            #print(r,c,d)
            assert G[r][c]=='.',(r,c)
            rr = (r+D[d][0])%R
            cc = (c+D[d][1])%C
            if G[rr][cc]==' ':
                (nr,nc,nd) = getDest(r,c,d,part)
                #print(f'r={r} c={c} rr={rr} cc={cc} nr={nr} nc={nc} region={getRegion(r,c)} d={d} newRegion={getRegion(nr,nc)} nd={nd}')
                if G[nr][nc]=='#':
                    break
                (r,c,d) = (nr,nc,nd)
                continue
            elif G[rr][cc]=='#':
                break
            else:
                r = rr
                c = cc
        if i==len(instr):
            break
        turn = instr[i]
        if turn == 'L':
            d = (d+3)%4
        elif turn == 'R':
            d = (d+1)%4
        else:
            assert False, (i,instr[i:],instr[i])
        i += 1
        #print('TURN', d)
    DV = {0:3,1:0,2:1,3:2}
    return ((r+1)*1000 + (c+1)*4 + DV[d])
print(solve(1))
print(solve(2))
