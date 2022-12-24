#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '17.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

# The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

def get_piece(t, y): # set of (x,y) pairs
    A = set()
    if t==0:
        return set([(2,y), (3,y), (4,y), (5,y)])
    elif t == 1:
        return set([(3, y+2), (2, y+1), (3,y+1), (4,y+1), (3,y)])
    elif t == 2:
        return set([(2, y), (3,y), (4,y), (4,y+1), (4,y+2)])
    elif t==3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t==4:
        return set([(2,y+1),(2,y),(3,y+1),(3,y)])
    else:
        assert False

def move_left(piece):
    if any([x==0 for (x,y) in piece]):
        return piece
    return set([(x-1,y) for (x,y) in piece])

def move_right(piece):
    if any([x==6 for (x,y) in piece]):
        return piece
    return set([(x+1,y) for (x,y) in piece])
def move_down(piece):
    return set([(x,y-1) for (x,y) in piece])
def move_up(piece):
    return set([(x,y+1) for (x,y) in piece])
def show(R):
    maxY = max([y for (x,y) in R])
    for y in range(maxY,0,-1):
        row = ''
        for x in range(7):
            if (x,y) in R:
                row += '#'
            else:
                row += ' '
        print(row)

R = set([(x,0) for x in range(7)])

def signature(R):
    maxY = max([y for (x,y) in R])
    return frozenset([(x,maxY-y) for (x,y) in R if maxY-y<=30])

L = 1000000000000

SEEN = {}
top = 0
i = 0
t = 0
added = 0
while t<L:
    #print(t, len(SEEN))
    piece = get_piece(t%5, top+4)
    while True:
        # pushed -> down
        if data[i]=='<':
            piece = move_left(piece)
            if piece & R:
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & R:
                piece = move_left(piece)
        i = (i+1)%len(data)
        piece = move_down(piece)
        if piece & R:
            piece = move_up(piece)
            R |= piece
            top = max([y for (x,y) in R])

            SR = (i, t%5, signature(R))
            if SR in SEEN and t>=2022:
                (oldt, oldy) = SEEN[SR]
                dy = top-oldy
                dt = t-oldt
                amt = (L-t)//dt
                added += amt*dy
                t += amt*dt
                assert t<=L
            SEEN[SR] = (t,top)
            #show(R)
            break
    t += 1
    if t==2022:
        print(top)
print(top+added)
