import fileinput
import re
from copy import deepcopy
from collections import defaultdict
import math

R = 10
C = 10

def rotate(T):
    TR = len(T)
    TC = len(T[0])
    # takes (r,c) to (c, R-1-r)
    RET = [['?' for _ in range(TR)] for _ in range(TC)]
    for r in range(TR):
        for c in range(TC):
            RET[c][TR-1-r] = T[r][c]
    return RET

def flip(T):
    return list(reversed(T))
def flip2(T):
    return [list(reversed(row)) for row in T]

def poss(T):
    ans = set()
    flips = [deepcopy(T), flip(T)] #, flip2(T), flip(flip2(T))]
    for _ in range(4):
        for i in range(len(flips)):
            ans.add(tuple([tuple(row) for row in flips[i]]))
            flips[i] = rotate(flips[i])
    return ans

L = list([l.strip() for l in fileinput.input()])
L.append('')
G = {}
name = None
piece = []
for l in L:
    if 'Tile' in l:
        name = int(l.split()[1][:-1])
    elif l:
        piece.append(list(l))
    else:
        G[name] = piece
        piece = []

#for k,T in G.items():
#    print(k)
#    for row in T:
#        print(''.join(row))

EDGE = {}
for k,T in G.items():
    left = []
    right = []
    top = []
    bottom = []
    for r in range(R):
        left.append(T[r][0])
        right.append(T[r][R-1])
    for c in range(C):
        top.append(T[0][c])
        bottom.append(T[R-1][c])
    edges = [tuple(x) for x in [left,right,top,bottom]]
    EDGE[k] = set([x for x in edges] + [tuple(reversed(x)) for x in edges])


E = defaultdict(set)

# Assumes if two pieces have identical boundaries they will actually be adjacent in the final puzzle
start = None
ans = 1
for k1,ET in EDGE.items():
    nbrs = 0
    for k2,EU in EDGE.items():
        if k1!=k2:
            if ET & EU:
                E[k1].add(k2)
    if len(E[k1]) == 2:
        start = k1
        ans *= k1
print(ans)

GR = int(math.sqrt(len(EDGE)))
GC = int(math.sqrt(len(EDGE)))
USED = set()
assert len(EDGE) == GR*GC
PLACE = [[None for _ in range(GR)] for _ in range(GC)]
PLACE[0][0] = start
PLACE[0][1],PLACE[1][0] = E[start]
USED.add(PLACE[0][0])
USED.add(PLACE[0][1])
USED.add(PLACE[1][1])

D = [(-1,0),(0,1),(1,0),(0,-1)]

#####
####
###
##
#

while True:
    if len(USED) == GR*GC:
        break
    for r in range(GR):
        for c in range(GC):
            if PLACE[r][c] is not None:
                continue
            opts = set([k for k in E.keys() if k not in USED])
            for dr,dc in D:
                rr,cc = r+dr,c+dc
                if 0<=rr<GR and 0<=cc<GC and PLACE[rr][cc]:
                    opts = opts & E[PLACE[rr][cc]]
            if len(opts) == 1:
                chosen = list(opts)[0]
                PLACE[r][c] = chosen
                assert chosen not in USED
                USED.add(chosen)

# Does the boundary of p1 match p2, assuming p2 is in the direction (dr,dc)?
def matches(p1,p2,dr,dc):
    if dr==-1: # up, so top of p1 should match bottom of p2
        for c in range(C):
            if p1[0][c]!=p2[R-1][c]:
                return False
        return True
    elif dc==1: # right, so right of p1 should match left of p2
        for r in range(R):
            if p1[r][C-1] != p2[r][0]:
                return False
        return True
    elif dr==1:
        for c in range(C):
            if p1[R-1][c] != p2[0][c]:
                return False
        return True
    elif dc==-1:
        for r in range(R):
            if p1[r][0] != p2[r][C-1]:
                return False
        return True
    else:
        assert False


PIECES = [[None for _ in range(GR)] for _ in range(GC)]
for r in range(GR):
    for c in range(GC):
        opts = poss(G[PLACE[r][c]])
        for dr,dc in D:
            rr,cc = r+dr,c+dc
            if 0<=rr<GR and 0<=cc<GC:
                ok_nbr = set()
                opts_nbr = poss(G[PLACE[rr][cc]])
                for o1 in opts:
                    for o2 in opts_nbr:
                        if matches(o1,o2,dr,dc):
                            ok_nbr.add(o1)
                opts = opts & ok_nbr
        # Assumes that every piece has only one orientation that can match its neighbors
        assert len(opts) == 1
        PIECES[r][c] = list(opts)[0]

for r in range(GR):
    for c in range(GC):
        for dr,dc in D:
            rr,cc = r+dr,c+dc
            if 0<=rr<GR and 0<=cc<GC:
                p1 = PIECES[r][c]
                p2 = PIECES[rr][cc]
                assert matches(p1,p2,dr,dc)

IMAGE = [['?' for _ in range(GC*(C-2))] for _ in range(GR*(R-2))]
for r in range(GR):
    for c in range(GC):
        T = PIECES[r][c]
        assert T in poss(G[PLACE[r][c]])
        for rr in range(1,len(T)-1):
            for cc in range(1,len(T[rr])-1):
                IMAGE[r*(R-2)+(rr-1)][c*(C-2)+(cc-1)] = T[rr][cc]

M = ['                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ']
MR = len(M)
MC = len(M[0])
for row in M:
    assert len(row)==MC

IR = len(IMAGE)
IC = len(IMAGE[0])
assert len(IMAGE) == IR
for row in IMAGE:
    assert len(row) == IC

for IM in poss(IMAGE):
    assert len(IM) == IR
    assert len(IM[0]) == IC
    IS_M = [[False for _ in range(len(IM[0]))] for _ in range(len(IM))]
    has_monster = False
    for r in range(IR):
        for c in range(IC):
            is_monster = True
            for mr in range(MR):
                for mc in range(MC):
                    if not (0<=r+mr<IR and 0<=c+mc<IC):
                        is_monster = False
                    else:
                        if M[mr][mc]=='#' and IM[r+mr][c+mc]!='#':
                            is_monster = False
            if is_monster:
                has_monster = True
                for mr in range(MR):
                    for mc in range(MC):
                        if M[mr][mc]=='#':
                            IS_M[r+mr][c+mc] = True
    # Assumes only one orientation has sea monsters
    if has_monster:
        ans = 0
        for r in range(IR):
            for c in range(IC):
                if IM[r][c]=='#' and not IS_M[r][c]:
                    ans += 1
        print(ans)
