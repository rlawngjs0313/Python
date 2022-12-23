import sys

N, K = map(int, sys.stdin.readline().split())
L1 = []
temp = input()

for i in temp:
    while L1 != [] and L1[-1] < i and K > 0:
        L1.pop()
        K -= 1
    L1.append(i)

if K > 0:
    print(''.join(L1[:-K]))
else:
    print(''.join(L1))