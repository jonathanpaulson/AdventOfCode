import fileinput
import re

L = list(l.strip() for l in fileinput.input())
limits = []
mine = None
other = []
for l in L:
    ints = [int(x) for x in re.findall('\d+', l)]
    if len(ints) == 4:
        limits.append(ints)
    elif len(ints) > 4:
        if mine is None:
            mine = ints
        else:
            other.append(ints)

n = len(limits)
assert n == 20

p1 = 0
OK = [[True for _ in range(n)] for _ in range(n)]

for vs in other:
    assert len(vs) == len(limits)
    ticket_valid = True
    for v in vs:
        valid = False
        for a,b,c,d in limits:
            if a<=v<=b or c<=v<=d:
                valid = True
        if not valid:
            p1 += v
            ticket_valid = False

    if ticket_valid:
        for i,v in enumerate(vs):
            for j,(a,b,c,d) in enumerate(limits):
                if not (a<=v<=b or c<=v<=d):
                    OK[i][j] = False

print(p1)

MAP = [None for _ in range(20)]
USED = [False for _ in range(20)]
found = 0
while True:
    for i in range(20):
        valid_j = [j for j in range(20) if OK[i][j] and not USED[j]]
        if len(valid_j) == 1:
            MAP[i] = valid_j[0]
            USED[valid_j[0]] = True
            found += 1
    if found == 20:
        break

#print(MAP)
p2 = 1
for i,j in enumerate(MAP):
    if j<6:
        p2 *= mine[i]
print(p2)
