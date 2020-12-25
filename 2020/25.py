import re
import sys


def transform(x, sz):
    #if sz == 0:
    #    return 1
    #elif sz % 2 == 0:
    #    return transform((x*x)%20201227, sz/2)
    #else:
    #    return (x*transform(x, sz-1))%20201227
    return pow(x, sz, 20201227)
    #v = 1
    #for _ in range(sz):
    #    v = v*x
    #    v = v%20201227
    #return v

k1,k2 = [int(x) for x in sys.stdin.read().strip().split('\n')]
#k1,k2 = 5764801,17807724

l1 = 0
while transform(7, l1) != k1:
    l1 += 1

l2 = 0
while transform(7, l2) != k2:
    l2 += 1

encryption = transform(k1, l2)
assert encryption == transform(k2, l1)
print(encryption)
