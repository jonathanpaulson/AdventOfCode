import sys
import z3
import re
import heapq
import functools
from collections import defaultdict, Counter, deque
from copy import deepcopy
from sympy.solvers.solveset import linsolve
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '21.in'
ans = 0
D = open(infile).read().strip()

pad1 = ['789', '456', '123', ' 0A']
pad2 = [' ^A', '<v>']
def getPad1(p1):
    r,c = p1
    if not (0<=r<len(pad1) and 0<=c<len(pad1[r])):
        return None
    if pad1[r][c]==' ':
        return None
    return pad1[r][c]
def getPad2(p):
    r,c = p
    if not (0<=r<len(pad2) and 0<=c<len(pad2[r])):
        return None
    if pad2[r][c]==' ':
        return None
    return pad2[r][c]

def applyPad1(p, move):
    if move == 'A':
        return (p, getPad1(p))
    elif move=='<':
        return ((p[0], p[1]-1), None)
    elif move=='^':
        return ((p[0]-1, p[1]), None)
    elif move=='>':
        return ((p[0], p[1]+1), None)
    elif move=='v':
        return ((p[0]+1, p[1]), None)

def applyPad2(p, move):
    if move == 'A':
        return (p, getPad2(p))
    elif move=='<':
        return ((p[0], p[1]-1), None)
    elif move=='^':
        return ((p[0]-1, p[1]), None)
    elif move=='>':
        return ((p[0], p[1]+1), None)
    elif move=='v':
        return ((p[0]+1, p[1]), None)

def solve1(code,pads):
    start = [0, (3,2), 'A', '', '']
    Q = []
    heapq.heappush(Q, start)
    SEEN = {}
    while Q:
        d,p1,p2,out,path = heapq.heappop(Q)
        assert p2 in ['<', '>', 'v', '^', 'A']
        if out==code:
            return d
        if not code.startswith(out):
            continue
        if getPad1(p1) is None:
            continue
        key = (p1,p2,out)
        if key in SEEN:
            assert d>=SEEN[key], f'{key=} {d=} {SEEN[key]=}'
            continue
        SEEN[key] = d
        for move in ['^', '<', 'v', '>', 'A']:
            new_p1 = p1
            new_out = out
            new_p1, output = applyPad1(p1, move)
            if output is not None:
                new_out = out + output
            cost_move = cost2(move,p2,pads)
            new_path = path #+ cost_move
            assert cost_move >= 0
            heapq.heappush(Q, [d+cost_move, new_p1, move, new_out, new_path])

def cost2_slow(ch, prev_move, pads):
    start_pos = {'^': (0,1), '<': (1,0), 'v': (1,1), '>': (1,2), 'A': (0,2)}[prev_move]
    start = [0, start_pos, '']
    for _ in range(pads-1):
        start.append((0,2))
    Q = deque([start])
    SEEN = set()
    while Q:
        d,p1,path,*ps = Q.popleft()
        key = (p1,tuple(ps))
        if key in SEEN:
            continue
        if getPad2(p1) is None:
            continue
        ok = True
        for p in ps:
            if getPad2(p) is None:
                ok = False
                break
        if not ok:
            continue
        SEEN.add(key)
        for move in ['^', '<', 'v', '>', 'A']:
            new_p1 = p1
            new_ps = deepcopy(ps)
            new_move = move
            for i,p in reversed(list(enumerate(ps))):
                new_ps[i], new_move = applyPad2(ps[i], new_move)
                if new_move is None:
                    break
                else:
                    for j in range(len(ps)):
                        if j > i:
                            assert new_ps[j] == (0,2)
            if new_move is not None:
                new_p1, output = applyPad2(p1, new_move)
                if output == ch:
                    return path+move
            Q.append([d+1, new_p1, path+move] + new_ps)
    assert False, f'{ch=} {prev_move=} {pads=}'

DP = {}
def cost2(ch, prev_move, pads):
    key = (ch,prev_move, pads)
    if key in DP:
        return DP[key]
    if pads==0:
        return 1
    else:
        assert ch in ['^', '>', 'v', '<', 'A']
        assert prev_move in ['^', '>', 'v', '<', 'A']
        assert pads>=1
        # cost of pressing ch with [pads] pads all of which are on A
        Q = []
        start_pos = {'^': (0,1), '<': (1,0), 'v': (1,1), '>': (1,2), 'A': (0,2)}[prev_move]
        heapq.heappush(Q, [0, start_pos, 'A', '', ''])
        SEEN = {}
        while Q:
            d,p,prev,out,path = heapq.heappop(Q)
            #print(d,p,prev,out,path)
            #assert d==len(path), f'{d=} {len(path)=} {path=}'
            if getPad2(p) is None:
                continue
            if out == ch:
                #assert len(path) == d, f'{new_path=} {new_d=}'
                #slow_path = cost2_slow(ch, prev_move, pads)
                #assert len(path) == len(slow_path), f'{ch=} {prev_move=} {pads=} {len(path)=} {len(slow_path)=} {path=} {slow_path=}'
                #print(f'{key=} {DP[key]=}')
                DP[key] = d
                return d
            elif len(out)>0:
                continue
            seen_key = (p,prev)
            if seen_key in SEEN:
                assert d>=SEEN[seen_key]
                continue
            SEEN[seen_key] = d
            for move in ['^', '<', 'v', '>', 'A']:
                new_p, output = applyPad2(p, move)
                cost_move = cost2(move, prev, pads-1)
                new_d = d + cost_move #len(cost_move)
                new_path = path #+ cost_move
                new_out = out
                if output is not None:
                    new_out = new_out + output
                heapq.heappush(Q, [new_d, new_p, move, new_out, new_path])
        assert False, f'{ch=} {pads=}'

def solve2(code):
    start = [0, (0,2), '', '']
    Q = deque([start])
    SEEN = set()
    while Q:
        d,p,out,path = Q.popleft()
        key = (p,out)
        if out==code:
            yield path
        if not code.startswith(out):
            continue
        if key in SEEN:
            continue
        SEEN.add(key)
        if getPad2(p) is None:
            continue
        for move in ['^', '<', 'v', '>', 'A']:
            new_p = p
            new_out = out
            new_p, output = applyPad2(p, move)
            if output is not None:
                new_out = out + output
            heapq.heappush(Q, [d+1, new_p, new_out, path+move])

def solve(code):
    pads = int(sys.argv[2])
    return solve1(code, pads)


#PADS = int(sys.argv[2])
# three copies of pad2; one copy of pad1
#One directional keypad that you are using.
#Two directional keypads that robots are using.
#One numeric keypad (on a door) that a robot is using.
def slowSolve(code, PADS):
    start = [0, (3,2), '', '']
    for _ in range(PADS):
        start.append((0,2))
    Q = deque([start])
    SEEN = set()
    while Q:
        d,p1,out,path,*ps = Q.popleft()
        key = (p1,out,tuple(ps))
        if out==code:
            return path
        if not code.startswith(out):
            continue
        if key in SEEN:
            continue
        if getPad1(p1) is None:
            continue
        ok = True
        for p in ps:
            if getPad2(p) is None:
                ok = False
                break
        if not ok:
            continue
        SEEN.add(key)
        if len(SEEN) % 10**5 == 0:
            print(len(SEEN), key)
        for move in ['^', '<', 'v', '>', 'A']:
            new_p1 = p1
            new_out = out
            new_ps = deepcopy(ps)
            new_move = move

            for i,p in reversed(list(enumerate(ps))):
                new_ps[i], new_move = applyPad2(ps[i], new_move)
                if new_move is None:
                    break
                else:
                    for j in range(len(ps)):
                        if j > i:
                            assert new_ps[j] == (0,2)
            if new_move is not None:
                new_p1, output = applyPad1(p1, new_move)
                if output is not None:
                    new_out = out + output
            Q.append([d+1, new_p1, new_out, path+move] + new_ps)

p1 = 0
p2 = 0
for line in D.split('\n'):
    s1 = solve1(line, 2)
    s2 = solve1(line, 25)
    #slow = slowSolve(line, int(sys.argv[2]))
    #assert len(score) == len(slow), f'{len(score)=} {len(slow)=}\n{score}\n{slow}'
    line_int = ints(line)[0]
    p1 += line_int * s1
    p2 += line_int * s2
pr(p1)
pr(p2)
