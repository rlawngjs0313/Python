import sys
N = int(input())
L1 = []
for i in range(N):
    A, B = map(str, sys.stdin.readline().rstrip().split())
    L1.append((int(A), B, i))
L1.sort(key=lambda x : (x[0], x[2]))
for i in L1:
    sys.stdout.write(f"{i[0]} {i[1]}"+'\n')