import sys
from collections import defaultdict, Counter

DP = {}
def F(line, i, used):
    if i==len(line) and used==12:
        return 0
    if i==len(line):
        return -10**20
    key = (i,used)
    if key in DP:
        return DP[key]
    ans = F(line, i+1, used)
    if used < 12:
        ans = max(ans, 10**(11-used)*int(line[i])+F(line, i+1, used+1))
    DP[key] = ans
    return ans


D = sys.stdin.read()
p1 = 0
p2 = 0
for line in D.splitlines():
    DP = {}
    p2 += F(line, 0, 0)

    best = None
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            score = int(line[i]+line[j])
            if best is None or score > best:
                best = score
    p1 += best
print(p1)
print(p2)
