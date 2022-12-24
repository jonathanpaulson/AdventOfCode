import sys

#W = [9,  2,  7,  9,  3,  9,  4,  9,  3,  8, 9, 7, 9, 4]

#    0   1   2   3   4   5   6   7   8   9 10 11 12 13
W = [5,  1,  1,  1,  1,  6,  1,  1,  1,  1, 1,  1,  1,  1]
Z = [1,  1,  1,  26, 1,  1,  1,  26, 26, 1, 26, 26, 26, 26]
X = [11, 14, 10, 0,  12, 12, 12, -8, -9, 11, 0, -5, -6, -12]
Y = [8,  13, 2,  7,  11, 4,  13, 13, 10, 1, 2, 14, 6, 14]
print(len([z for z in Z if z==26]))
print(len([x for x in X if x<10]))

w = int('9'*14)
while True:
  #w -= 1
  #W = [int(x) for x in reversed(str(w))]

  x = 0
  y = 0
  z = 0
  for i in range(14):
    z26 = z%26
    goal = z26 + X[i]
    if 1<=goal<=9:
      W[i] = goal

    z //= Z[i]
    x = (0 if W[i]==goal else 1)
    z *= (25 if x==1 else 0) + 1
    z += (W[i]+Y[i] if x==1 else 0)
    print(f'i={i} goal={goal} z%26={z26} X[i]={X[i]} Y[i]={Y[i]} W[i]={W[i]} Z[i]={Z[i]} z={[(z//26**i)%26 for i in range(14)]}')
    if X[i] < 10 and W[i]!=goal:
      break
  print(W, z, ''.join([str(x) for x in W]))
  if z==0:
    sys.exit(0)
  print()
  sys.exit(0)
