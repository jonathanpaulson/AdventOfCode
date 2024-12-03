import sys
import re
from collections import defaultdict, Counter
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else '3.in'
D = open(infile).read().strip()

p1 = 0
p2 = 0
enabled = True
for i in range(len(D)):
    if D[i:].startswith('do()'):
        enabled = True
    if D[i:].startswith("don't()"):
        enabled = False
    instr = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', D[i:])
    if instr is not None:
        x,y = int(instr.group(1)), int(instr.group(2))
        p1 += x*y
        if enabled:
            p2 += x*y
print(p1)
print(p2)
