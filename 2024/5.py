import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else '5.in'
p1 = 0
p2 = 0
D = open(infile).read().strip()

# E[x] is the set of pages that must come before x
# ER[x] is the set of pages that must come after x
E = defaultdict(set)
ER = defaultdict(set)
edges, queries = D.split('\n\n')
for line in edges.split('\n'):
    x,y = line.split('|')
    x,y = int(x), int(y)
    E[y].add(x)
    ER[x].add(y)

for query in queries.split('\n'):
    vs = [int(x) for x in query.split(',')]
    assert len(vs)%2==1
    ok = True
    for i,x in enumerate(vs):
        for j,y in enumerate(vs):
            if i<j and y in E[x]:
                ok = False
    if ok:
        p1 += vs[len(vs)//2]
    else:
        good = []
        Q = deque([])
        D = {v: len(E[v] & set(vs)) for v in vs}
        for v in vs:
            if D[v] == 0:
                Q.append(v)
        while Q:
            x = Q.popleft()
            good.append(x)
            for y in ER[x]:
                if y in D:
                    D[y] -= 1
                    if D[y] == 0:
                        Q.append(y)
        p2 += good[len(good)//2]
pr(p1)
pr(p2)
