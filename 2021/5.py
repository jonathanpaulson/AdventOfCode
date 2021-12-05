import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv)>1 else '5.in'

G1 = defaultdict(int)
G2 = defaultdict(int)
for line in open(infile):
    start,end = line.split('->')
    x1,y1 = start.split(',')
    x2,y2 = end.split(',')
    x1 = int(x1.strip())
    y1 = int(y1.strip())
    x2 = int(x2.strip())
    y2 = int(y2.strip())

    dx = x2-x1
    dy = y2-y1

    for i in range(1+max(abs(dx),abs(dy))):
        x = x1+(1 if dx>0 else (-1 if dx<0 else 0))*i
        y = y1+(1 if dy>0 else (-1 if dy<0 else 0))*i
        if dx==0 or dy==0:
            G1[(x,y)] += 1
        G2[(x,y)] += 1

print(len([k for k in G1 if G1[k]>1]))
print(len([k for k in G2 if G2[k]>1]))
