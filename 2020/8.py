import fileinput
import re
from copy import deepcopy
from collections import namedtuple

class Instr(object):
    def __init__(self, op, arg):
        self.op = op
        self.arg = int(arg)
    def __repr__(self):
        return '{} {}'.format(self.op, self.arg)

def run(P, ip, acc):
    cmd = P[ip]
    if cmd.op == 'acc':
        acc += cmd.arg
        ip += 1
    elif cmd.op == 'nop':
        ip += 1
    elif cmd.op == 'jmp':
        ip += cmd.arg
    return (ip, acc)

P = list([Instr(*l.split()) for l in fileinput.input()])
ip = 0
acc = 0
seen = set()
while True:
    if ip in seen:
        print(acc)
        break
    seen.add(ip)
    ip, acc = run(P, ip, acc) 

for change in range(len(P)):
    Pmod = deepcopy(P)
    if Pmod[change].op == 'nop':
        Pmod[change].op = 'jmp'
    elif Pmod[change].op == 'jmp':
        Pmod[change].op = 'nop'
    else:
        continue
    t = 0
    ip = 0
    acc = 0
    while 0<=ip<len(Pmod) and t<1000:
        t += 1
        ip, acc = run(Pmod, ip, acc)
    if ip == len(Pmod):
        print(acc)
        break
