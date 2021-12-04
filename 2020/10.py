import fileinput
import re

p1 = 0
p2 = 0

xs = [int(x) for x in list(fileinput.input())]
xs.append(0)
xs = sorted(xs)
xs.append(max(xs)+3)
n1 = 0
n3 = 0
for i in range(len(xs)-1):
    d = xs[i+1]-xs[i]
    if d==1:
        n1 += 1
    elif d==3:
        n3 += 1

# dynamic programming
DP = {}
# dp(i) = the number of ways to complete the adapter chain given
#         that you are currently at adapter xs[i]
def dp(i):
    if i==len(xs)-1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(xs)):
        if xs[j]-xs[i]<=3:
            # one way to get from i to the end is to first step to j
            # the number of paths from i that *start* by stepping to xs[j] is just DP[j]
            # So dp(i) = \sum_{valid j} dp(j)
            ans += dp(j)
    DP[i] = ans
    return ans

print(n1*n3)
print(dp(0))
