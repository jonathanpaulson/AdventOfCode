def score(c):
    if 'a'<=c<='z':
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 1 + 26


p1 = 0
for line in open('3.in'):
    x = line.strip()
    assert len(x)%2 == 0
    y,z = x[:len(x)//2], x[len(x)//2:]
    for c in y:
        if c in z:
            p1 += score(c)
            break
print(p1)

p2 = 0
X = [line for line in open('3.in')]
i = 0
while i < len(X):
    for c in X[i]:
        if c in X[i+1] and c in X[i+2]:
            p2 += score(c)
            break
    i += 3
print(p2)
