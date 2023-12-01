import fileinput
import re
import itertools

def solve(p1):
    ON = set()
    L = list([l.strip() for l in fileinput.input()])
    for r,l in enumerate(L):
        for c,ch in enumerate(l):
            if ch == '#':
                ON.add((r,c,0,0))

    for _ in range(6):
        NEW_ON = set()
        CHECK = set()
        for (x,y,z,w) in ON:
            for dx,dy,dz,dw in itertools.product([-1,0,1], repeat=4):
                if w+dw==0 or (not p1):
                    CHECK.add((x+dx, y+dy, z+dz, w+dw))

        for (x,y,z,w) in CHECK:
            nbr = 0
            for dx,dy,dz,dw in itertools.product([-1,0,1], repeat=4):
                if dx!=0 or dy!=0 or dz!=0 or dw!=0:
                    if (x+dx, y+dy, z+dz, w+dw) in ON:
                        nbr += 1
            if (x,y,z,w) not in ON and nbr == 3:
                NEW_ON.add((x,y,z,w))
            if (x,y,z,w) in ON and nbr in [2,3]:
                NEW_ON.add((x,y,z,w))
        ON = NEW_ON

    return len(ON)

print(solve(True))
print(solve(False))
