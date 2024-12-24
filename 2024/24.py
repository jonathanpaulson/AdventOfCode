import sys
import z3
import re
import heapq
import functools
from collections import defaultdict, Counter, deque
from copy import deepcopy
from sympy.solvers.solveset import linsolve
import random
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left
def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

infile = sys.argv[1] if len(sys.argv)>=2 else '24.in'
D = open(infile).read().strip()

values, gates = D.split('\n\n')

def doOp(v1,v2,op):
    if op=='AND':
        #return v1&v2
        return f'({v1} AND {v2})'
    elif op=='OR':
        #return v1|v2
        return f'({v1} OR {v2})'
    elif op=='XOR':
        return f'({v1} XOR {v2})'
        #return v1^v2
    else:
        assert False, op

gates = gates.split('\n')
gates = [g.split() for g in gates]

print('strict digraph {')
for gate in gates:
    n1,op,n2,arrow,n3 = gate
    print(f'  {n1} -> {n3} [label={op}]')
    print(f'  {n2} -> {n3} [label={op}]')
print('}')
assert False


def run(gates):
    WRONG = set()
    for _ in range(10):
        X = random.randint(0, 2**45)
        Y = random.randint(0, 2**45)

        V = {}
        for line in values.split('\n'):
            name, value = line.split(': ')
            idx = int(name[1:])
            if name.startswith('x'):
                V[name] = name #(X>>idx)%2
            elif name.startswith('y'):
                V[name] = name #(Y>>idx)%2
            else:
                assert False, name

        idxs = []
        while True:
            changed = False
            for i,gate in enumerate(gates):
                words = gate
                n1 = words[0]
                op = words[1]
                n2 = words[2]
                n3 = words[4]
                if n1 in V and n2 in V and n3 not in V:
                    idxs.append(i)
                    V[n3] = doOp(V[n1],V[n2],op)
                    print(i,n1,n2,n3,V[n1],V[n2],V[n3])
                    changed = True
            if not changed:
                break
        #assert False, idxs

        C = X+Y
        Z = 0
        for k,v in sorted(V.items()):
            if k.startswith('z'):
                print(k,v)
                idx = int(k[1:])
                #Z += 2**idx * v
        assert False
        for bit in range(45):
            zbit = (Z>>bit)%2
            correct_bit = (C>>bit)%2
            if zbit != correct_bit:
                WRONG.add(bit)
    return WRONG

def swapGates(gates, i1, i2):
    tmp = gates[i1][4]
    gates[i1][4] = gates[i2][4]
    gates[i2][4] = tmp
    return gates

w0 = run(gates)
OUT = set()
SWAPS = [] #(6,127)]
for (i0,i1) in SWAPS:
    print(gates[i0], gates[i1])
    gates = swapGates(gates, i0, i1)

print(w0, len(gates))
while len(SWAPS) < 4:
    best = None
    for i0 in range(len(gates)):
        for i1 in range(len(gates)):
            new_gates = swapGates(gates, i0, i1)
            new_score = run(new_gates)
            if best is None or min(new_score) > min(best[0]):
                print(new_score, i0, i1, gates[i0], gates[i1])
                best = (new_score,i0,i1)
            new_gates = swapGates(gates, i0, i1)
    print(best)
    SWAPS.append((best[1], best[2]))
    OUT.add(gates[best[1]][4])
    OUT.add(gates[best[2]][4])
    gates = swapGates(gates, best[1], best[2])
pr(','.join(sorted(OUT)))
    #if new_score < w0:
    #    gates = new_gates
    #    w0 = new_score
    #    print(new_score,i0,i1)
    #    OUT.add(gates[i0][4])
    #    OUT.add(gates[i1][4])
    #    if new_score == 0:
    #        print(','.join(sorted(OUT)))
    #else:
    #    swapGates(gates, i0, i1)
