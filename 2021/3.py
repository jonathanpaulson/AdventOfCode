import sys

infile = sys.argv[1] if len(sys.argv)>1 else '3.in'

N = []
for line in open(infile):
    line = line.strip()
    N.append(line)
width = len(N[0])
for x in N:
    assert len(x) == width
# V is 2 x width
V = [[0 for _ in range(width)] for _ in range(2)]
for x in N:
    for i,c in enumerate(x):
        V[1 if c=='1' else 0][i] += 1
gamma = ''
epsilon = ''
for i in range(width):
    if V[0][i] > V[1][i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma,2)*int(epsilon,2))

A = list(N)
B = list(N)
for i in range(width):
    if len(A) > 1:
        a0 = len([x  for x in A if x[i]=='0'])
        a1 = len([x  for x in A if x[i]=='1'])
        if a1 >= a0:
            A = [x for x in A if x[i]=='1']
        else:
            A = [x for x in A if x[i]=='0']
    if len(B) > 1:
        b0 = len([x  for x in B if x[i]=='0'])
        b1 = len([x  for x in B if x[i]=='1'])
        if b1 >= b0:
            B = [x for x in B if x[i]=='0']
        else:
            B = [x for x in B if x[i]=='1']
print(int(A[0],2)*int(B[0],2))
