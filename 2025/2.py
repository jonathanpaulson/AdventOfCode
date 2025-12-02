import sys
from collections import defaultdict, Counter

def invalid(x,p2):
    x = str(x)
    for k in range(2,len(x)+1 if p2 else 3):
        if len(x)%k==0:
            ok = True
            sz = len(x)//k
            i = 0
            while i < len(x):
                if x[i:i+sz]!=x[:sz]:
                    ok = False
                i += sz
            if ok:
                return True
    return False

D = sys.stdin.read()
p1 = 0
p2 = 0
ranges = D.split(',')
for r in ranges:
    first,last = r.split('-')
    first = int(first)
    last = int(last)
    for x in range(first, last+1):
        if invalid(x,False):
            p1 += x
        if invalid(x,True):
            p2 += x
print(p1)
print(p2)
