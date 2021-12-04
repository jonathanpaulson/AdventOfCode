import fileinput
import re
from collections import defaultdict

L = list([l.strip() for l in fileinput.input()])
FOODS = []
for l in L:
    first, rest = l.split('(contains ')
    I = set(first.split())
    A = set(rest[:-1].split(', '))
    FOODS.append((I,A))

all_I = set()
all_A = set()
for I,A in FOODS:
    all_A |= A
    all_I |= I

# in allergens -> corresponding ingredient in list

COULD_BE = {i: set(all_A) for i in all_I}
C = defaultdict(int)
for I,A in FOODS:
    for i in I:
        C[i] += 1

    # for each allergen, all the missing ingredients are definitely not it
    # this is the only thing you can deduce!
    for a in A:
        for i in all_I:
            if i not in I:
                COULD_BE[i].discard(a)

MAPPING = {}
USED = set()

p1 = 0
for i in all_I:
    if not COULD_BE[i]:
        p1 += C[i]
print(p1)

while len(MAPPING) < len(all_A):
    for i in all_I:
        poss = [a for a in COULD_BE[i] if a not in USED]
        if len(poss)==1:
            MAPPING[i] = poss[0]
            USED.add(poss[0])
sorted_i = ','.join([k for k,v in sorted(MAPPING.items(), key=lambda kv:kv[1])])
print(sorted_i)
