import fileinput
import re

def range_for(idx, ON):
    return range(min(p[idx] for p in ON)-1, max(p[idx] for p in ON)+2)

def solve(p1):
    ON = set()
    L = list([l.strip() for l in fileinput.input()])
    for r,l in enumerate(L):
        for c,ch in enumerate(l):
            if ch == '#':
                ON.add((r,c,0,0))

    for _ in range(6):
        NEW_ON = set()
        w_range = ([0] if p1 else range_for(3, ON))
        for x in range_for(0, ON):
            for y in range_for(1, ON):
                for z in range_for(2, ON):
                    for w in w_range:
                        nbr = 0
                        for dx in [-1,0,1]:
                            for dy in [-1,0,1]:
                                for dz in [-1,0,1]:
                                    for dw in [-1,0,1]:
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
