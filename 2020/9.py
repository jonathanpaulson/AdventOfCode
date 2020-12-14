import fileinput
import re
import itertools

PRE = 25
xs = list([int(x) for x in fileinput.input()])

p1 = None
for i in range(PRE, len(xs)):
    prev = xs[i-PRE:i]
    if p1 is None and (not any([x+y==xs[i] for x,y in itertools.combinations(prev, 2)])):
        p1 = xs[i]

p2 = None
for i in range(len(xs)):
    for j in range(i+2, len(xs)):
        ys = xs[i:j]
        if sum(ys)==p1:
            assert p2 is None
            p2 = min(ys)+max(ys)
print(p1)
print(p2)
