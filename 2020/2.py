import fileinput
from collections import defaultdict

p1 = 0
p2 = 0
lines = list(fileinput.input())
for line in lines:
    # 5-6 s: zssmssbsms
    words = line.strip().split()
    lo,hi = [int(x) for x in words[0].split('-')]
    ch_req = words[1][0]
    password = words[2]
    counts = defaultdict(int)
    for ch in password:
        counts[ch] += 1
    if lo <= counts[ch_req] <= hi:
        p1 += 1
    if (password[lo-1]==ch_req) ^ (password[hi-1]==ch_req):
        p2 += 1
print(p1)
print(p2)
