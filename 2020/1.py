import sys
import fileinput

X = [int(line) for line in fileinput.input()]
n = len(X)
for i in range(n):
    for j in range(i+1, n):
        if X[i]+X[j]==2020:
            print('Part 1:', X[i]*X[j])
        for k in range(j+1, n):
            if X[i]+X[j]+X[k]==2020:
                print('Part 2:', X[i]*X[j]*X[k])
