#!/usr/bin/python3
import sys
import heapq
import itertools
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(int(1e6))

infile = sys.argv[1] if len(sys.argv)>1 else '16.in'
data = open(infile).read().strip()
binary = bin(int(data, 16))[2:]
while len(binary) < 4*len(data):
    binary = '0'+binary
assert len(binary)%4==0
assert len(binary) == 4*len(data)

p1 = 0
def parse(bits, i, indent):
    """Takes the bitstream, a start index, and the depth of the packet.
    Return (eval of packet, next bit after this packet)
    """
    # bits[a:b] means [a,b), so the next interval is [b,...)
    global p1
    version = int(bits[i+0:i+3], 2)
    p1 += version
    type_ = int(bits[i+3:i+6], 2)
    indent_str = (' '*indent)
    #print(f'{indent_str}i={i} version={version} type={type_} {len(binary)}')
    if type_ == 4: # lit
        i += 6
        v = 0
        while True:
            v = v*16 + int(bits[i+1:i+5], 2)
            i += 5
            if bits[i-5] == '0':
                return v,i
        assert False
    else:
        len_id = int(bits[i+6], 2)
        vs = []
        if len_id == 0:
            len_bits = int(bits[i+7:i+7+15], 2)
            #print(f'len_bits={len_bits} {bits[i+7:i+7+15]}')
            start_i = i+7+15
            i = start_i
            while True:
                v, next_i = parse(bits, i, indent+1)
                #print(f'v={v} next_i={next_i}')
                vs.append(v)
                assert next_i > i
                assert next_i - start_i <= len_bits, f'next_i={next_i} start_i={start_i} len_bits={len_bits}'
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            n_packets = int(bits[i+7:i+7+11], 2)
            #print(f'n_packets={n_packets}')
            i += 7+11
            for t in range(n_packets):
                v, next_i = parse(bits, i, indent+1)
                #print(f'v={v} next_i={next_i}')
                vs.append(v)
                assert next_i > i
                i = next_i
        if type_ == 0:
            return sum(vs), i
        elif type_ == 1:
            ans = 1
            for v in vs:
                ans *= v
            return ans, i
        elif type_ == 2:
            return min(vs), i
        elif type_ == 3:
            return max(vs), i
        elif type_ == 5:
            return (1 if vs[0] > vs[1] else 0), i
        elif type_ == 6:
            return (1 if vs[0] < vs[1] else 0), i
        elif type_ == 7:
            return (1 if vs[0] == vs[1] else 0), i
        else:
            assert False, type_

value, next_i  = parse(binary, 0, 0)
assert len(binary)-4 < next_i <= len(binary)
print(p1)
print(value)
