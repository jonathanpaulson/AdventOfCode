#!/usr/bin/python3
import sys
import itertools
from collections import defaultdict, Counter

# 0: abcefg (6)
# 6: abdefg (6)
# 9: abcdfg (6)

# 2: acdeg (5)
# 3: acdfg (5)
# 5: abdfg (5)

# 1: cf (2)
# 4: bcdf (4)
# 7: acf (3)
# 8: abcdefg (7)

digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

def find_perm_slow(before):
    for perm in itertools.permutations(list(range(8))):
        ok = True
        D = {}
        for i in range(8):
            D[chr(ord('a')+i)] = chr(ord('a')+perm[i])
        for w in before:
            w_perm = ''
            for c in w:
                w_perm += D[c]
            w_perm = ''.join(sorted(w_perm))

            if w_perm not in digits.values():
                ok = False
        if ok:
            return D

def find_perm(before):
    A = {}
    for w in before:
        if len(w) == 2: # 1
            cf = w
    assert len(cf) == 2, cf
    for w in before:
        if len(w) == 6 and (cf[0] in w)!=(cf[1] in w): # 6
            if cf[0] in w:
                A[cf[0]] = 'f'
                A[cf[1]] = 'c'
            else:
                A[cf[1]] = 'f'
                A[cf[0]] = 'c'
    assert len(A) == 2, f'A={A} cf={cf} {before}'
    for w in before:
        if len(w)==3: # 7
            for c in w:
                if c not in cf:
                    A[c] = 'a'
    assert len(A) == 3, A
    for w in before:
        if len(w)==4: #4
            bd = ''
            for c in w:
                if c not in cf:
                    bd += c
    assert len(bd) == 2, bd
    # 0 is length-6 and missing one of b/d. B is present; D is missing.
    # 9 is length-6 missing one of e/g. G is present; E is missing.
    for w in before:
        if len(w)==6 and (bd[0] in w)!=(bd[1] in w): # 0
            if bd[0] in w:
                A[bd[0]] = 'b'
                A[bd[1]] = 'd'
            else:
                A[bd[1]] = 'b'
                A[bd[0]] = 'd'
    assert len(A) == 5, A
    eg = ''
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if c not in A:
            eg += c
    assert len(eg) == 2, eg
    for w in before:
        if len(w) == 6 and (eg[0] in w)!=(eg[1] in w): # 9
            if eg[0] in w:
                A[eg[0]] = 'g'
                A[eg[1]] = 'e'
            else:
                A[eg[1]] = 'g'
                A[eg[0]] = 'e'
    assert len(A) == 7, A
    return A

p1 = 0
ans = 0
infile = sys.argv[1] if len(sys.argv)>1 else '8.in'
for line in open(infile):
    before, after = line.split('|')
    before = before.split()
    after = after.split()


    D = find_perm(before)
    ret = ''
    for w in after:
        w_perm = ''
        for c in w:
            w_perm += D[c]
        w_perm = ''.join(sorted(w_perm))
        d = [k for k,v in digits.items() if v==w_perm]
        assert len(d)==1
        if d[0] in [1,4,7,8]:
            p1 += 1
        ret += str(d[0])
    ans += int(ret)
print(p1)
print(ans)
