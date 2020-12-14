import fileinput
import re
from copy import deepcopy

L = [list(l.strip()) for l in list(fileinput.input())]
R = len(L)
C = len(L[0])

def solve(L, p1):
    t = 0
    while True:
        t += 1
        #print('='*80)
        #for r in range(R):
        #    print(''.join(L[r]))

        newL = deepcopy(L)
        change = False
        for r in range(R): 
            for c in range(C):
                nocc = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if not (dr==0 and dc==0):
                            rr = r+dr
                            cc = c+dc
                            # Only skip floor in part 2
                            while 0<=rr<R and 0<=cc<C and L[rr][cc]=='.' and (not p1):
                                rr = rr+dr
                                cc = cc+dc
                            if 0<=rr<R and 0<=cc<C and L[rr][cc]=='#':
                                nocc += 1

                if L[r][c]=='L':
                    if nocc == 0:
                        newL[r][c] = '#'
                        change = True
                # Threshold changes from 4->5 in part 2
                elif L[r][c] == '#' and nocc>=(4 if p1 else 5):
                    newL[r][c] = 'L'
                    change = True
        if not change:
            break
        L = deepcopy(newL)

    print(t)
    ans = 0
    for r in range(R):
        for c in range(C):
            if L[r][c] == '#':
                ans += 1
    return ans

print(solve(L, True))
print(solve(L, False))
