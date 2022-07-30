import sys

L1 = [False]+[False]+[True]*(999999)

for i in range(1000):
    if L1[i] == True:
        for j in range(i*2, len(L1)-1, i):
            L1[j] = False

while True:
    n = int(sys.stdin.readline())
    index = 0
    if n == 0:
        break
    else:
        for i in range(3, 1000001):
            if L1[i] and L1[n-i]:
                sys.stdout.write(f"{n} = {i} + {n-i}" + '\n')
                break