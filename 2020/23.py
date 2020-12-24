import fileinput
import re
import sys

#start = '389125467'
start = '496138527'

def solve(is_p2):
    n = len(start) if (not is_p2) else int(1e6)
    N = [None for i in range(n+1)]
    X = [int(x) for x in start]
    for i in range(len(X)):
        N[X[i]] = X[(i+1)%len(X)]
    if is_p2:
        N[X[-1]] = len(X)+1
        for i in range(len(X)+1, n+1):
            N[i] = i+1
        N[-1] = X[0]

    t = 0 
    current = X[0]
    nmoves = int(1e7) if is_p2 else 100
    for _ in range(nmoves):
        t += 1
        pickup = N[current]
        N[current] = N[N[N[pickup]]]

        dest = n if current==1 else current-1
        while dest in [pickup, N[pickup], N[N[pickup]]]:
            dest = n if dest==1 else dest-1

        N[N[N[pickup]]] = N[dest]
        N[dest] = pickup
        current = N[current]

    if is_p2:
        return N[1]*N[N[1]]
    else:
        ans = []
        x = N[1]
        while x != 1:
            ans.append(x)
            x = N[x]
        return ''.join([str(x) for x in ans])
print(solve(False))
print(solve(True))
