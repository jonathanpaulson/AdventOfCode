#!/usr/bin/python3
import sys
from copy import deepcopy
infile = sys.argv[1] if len(sys.argv)>1 else '5.in'
data = open(infile).read()
lines = [x for x in data.split('\n')]

S = []
cmds = []
for line in lines:
    if line == '':
        break
    sz = (len(line)+1)//4
    while len(S) < sz:
        S.append([])
    for i in range(len(S)):
        ch = line[1+4*i]
        if ch != ' ' and 'A'<=ch<='Z':
            S[i].append(ch)
#print(S)

S1 = deepcopy(S)
S2 = deepcopy(S)
found = False
for cmd in lines:
    if cmd == '':
        found = True
        continue
    if not found:
        continue
    words = cmd.split()
    qty = int(words[1])
    from_ = int(words[3])-1
    to_ = int(words[5])-1
    for (ST, do_rev) in [(S1, True), (S2, False)]:
        MOVE = ST[from_][:qty]
        ST[from_] = ST[from_][qty:]
        ST[to_] = (list(reversed(MOVE)) if do_rev else MOVE) + ST[to_]
print(''.join([s[0] for s in S1 if len(s)>0]))
print(''.join([s[0] for s in S2 if len(s)>0]))
