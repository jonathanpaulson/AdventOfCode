import re
import sys

L = sys.stdin.read().strip().split('\n')
B = set()
for l in L:
    x,y,z = 0,0,0
    i = 0
    while l:
        if l.startswith('e'):
            x += 1
            y -= 1
            l = l[1:]
        elif l.startswith('se'):
            y -= 1
            z += 1
            l = l[2:]
        elif l.startswith('sw'):
            x -= 1
            z += 1
            l = l[2:]
        elif l.startswith('w'):
            x -= 1
            y += 1
            l = l[1:]
        elif l.startswith('nw'):
            z -= 1
            y += 1
            l = l[2:]
        elif l.startswith('ne'):
            x += 1
            z -= 1
            l = l[2:]
        else:
            assert False
    if (x,y,z) in B:
        B.remove((x,y,z))
    else:
        B.add((x,y,z))
print(len(B))

for _ in range(100):
    newB = set()
    CHECK = set()
    for (x,y,z) in B:
        CHECK.add((x,y,z))
        for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            CHECK.add((x+dx,y+dy,z+dz))

    for (x,y,z) in CHECK:
        nbr = 0
        for (dx,dy,dz) in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            if (x+dx,y+dy,z+dz) in B:
                nbr += 1
        if (x,y,z) in B and (nbr==1 or nbr==2):
            newB.add((x,y,z))
        if (x,y,z) not in B and nbr==2:
            newB.add((x,y,z))
    B = newB
print(len(B))
