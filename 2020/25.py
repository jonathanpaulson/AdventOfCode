import re
import sys


def transform(x, sz):
    return pow(x, sz, 20201227)

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
