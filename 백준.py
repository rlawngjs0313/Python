import sys

N = int(input())
L1 = []

for i in range(N):
    L1.append(int(sys.stdin.readline()))
for i in sorted(L1):
    sys.stdout.write(str(i)+'\n')