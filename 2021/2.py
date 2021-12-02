import sys

infile = sys.argv[1] if len(sys.argv)>1 else '2.in'

fwd1 = 0
depth1 = 0

fwd2 = 0
depth2 = 0
aim = 0

for line in open(infile):
    cmd,amt = line.split()
    amt = int(amt)
    if cmd == 'forward':
        fwd1 += amt
        fwd2 += amt
        depth2 += amt*aim
    elif cmd == 'up':
        depth1 -= amt
        aim -= amt
    else:
        assert cmd == 'down'
        depth1 += amt
        aim += amt
print(fwd1*depth1)
print(fwd2*depth2)
