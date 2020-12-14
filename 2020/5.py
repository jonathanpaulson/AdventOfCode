import fileinput
import re

p1 = None
p2 = None

ids = set()
lines = list(fileinput.input())
lines.append('')
for line in lines:
    line = line.strip()
    # FBFBBFFRLR
    # Translate to binary: row=0101100
    # 32+8+4 = row 44
    # col=101
    # 4+1 = col 5

    row = 0
    rp = 64

    col = 0
    cp = 4

    for c in line:
        if c == 'B':
            row += rp
            rp /= 2
        elif c == 'F':
            rp /= 2

        if c == 'R':
            col += cp
            cp /= 2
        elif c == 'L':
            cp /= 2

    seat_id = row*8+col
    ids.add(seat_id)
    if p1:
        p1 = max(p1, seat_id)
    else:
        p1 = seat_id

for id_ in sorted(ids):
    if id_+1 not in ids and id_+2 in ids:
        assert p2 is None
        p2 = id_+1

print(p1)
print(p2)
