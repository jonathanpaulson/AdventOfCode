import fileinput
import re

def gcd(x,y):
    if x==0:
        return y
    return gcd(y%x, x)

# Compute b**e modulo mod
def mod_pow(b, e, mod):
    if e==0:
        return 1
    elif e%2==0:
        # If E is even, a**E = (a^2)^(E/2)
        return mod_pow((b*b)%mod, e/2, mod)
    else:
        return (b*mod_pow(b,e-1,mod))%mod

# We want to find x s.t. (a*x)%m == 1
# Number theory fact: if m is prime, then a**(m-1)==1 for any a.
# Therefore, a**(m-2)*a == 1 for every a.
# So a**(m-2) is a modular inverse of a!
def mod_inverse(a, m):
    return mod_pow(a%m, m-2, m)

lines = list(fileinput.input())
t0 = int(lines[0])
B1 = [int(x) for x in lines[1].strip().split(',') if x!='x']
best = None
for b in B1:
    t = t0
    while t%b!=0:
        t += 1
    wait_time = t-t0
    if best is None or wait_time < best[0]:
        best = (wait_time, b)
print(best[0]*best[1])

# Part 2. We want to find time T.
B = lines[1].strip().split(',')
# Suppose bus K appears at index I in the list.
# K should depart at time T+I. i.e. T+I should be a multiple of K.
# T+I % K == 0
# T % K == -I
# T % K == (K-(I%K))%K (want 0<=RHS<K)

# Chinese remainder theorem: Let N be the product of the bus IDs in our input.
# There is exactly one T <N satisfying the constraints.

constraints = []
N = 1
for i,b in enumerate(B):
    if b!='x':
        b = int(b)
        i %= b
        constraints.append(((b-i)%b,b))
        N *= b

ans = 0
# x % b = i
for i,b in constraints:
    NI = N/b
    # NI is the product of the *other* bus IDs
    # If we add a multiple of NI to T, it won't affect when the other buses arrive modulo T,
    # since NI is a multiple of each other bus ID.
    # Is there a multiple of NI we can add to T so that T%b==i? Yes!
    # We want to find a multiple of NI s.t. (a*NI)%b == i
    # First find MI s.t. (MI*NI)%b == 1
    # Then (i*MI*NI)%b == i
    assert gcd(NI,b) == 1
    mi = mod_inverse(NI, b)
    assert mi == mod_inverse(NI, b)
    assert (mi*NI)%b == 1
    assert (i*mi*NI)%b == i
    for_b = i*mi*NI
    assert for_b%b == i
    assert for_b%NI == 0
    ans += for_b
    #print(i,ni,mi,b)

ans %= N
for i,b in constraints:
    assert ans%b == i

print(ans)
