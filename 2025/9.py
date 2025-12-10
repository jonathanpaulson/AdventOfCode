import shapely
import sys

D = sys.stdin.read()
ans = 0
P = []
G = set()
for line in D.splitlines():
    x,y = [int(x) for x in line.split(',')]
    P.append((x,y))
polygon = shapely.Polygon(P)
shapely.prepare(polygon)

ans1 = 0
ans2 = 0
for p1 in P:
    for p2 in P:
        corners = [p1, (p1[0], p2[1]), p2, (p2[0], p1[1])]
        area = abs(p1[0]-p2[0]+1)*abs(p1[1]-p2[1]+1)
        if area > ans1:
            ans1 = area
        rect = shapely.Polygon(corners)
        if polygon.contains(rect) and area > ans2:
            ans2 = area
print(ans1)
print(ans2)
