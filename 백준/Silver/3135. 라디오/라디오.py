import sys, bisect
input = sys.stdin.readline
print = sys.stdout.write

A, B = map(int, input().split())
N = int(input())
L1 = []

for _ in range(N):
    L1.append(int(input()))

L1.sort()
idx = bisect.bisect_left(L1,B)

if idx == 0:
    print(f"{min(abs(L1[idx]-B)+1,abs(A-B))}")
elif idx == N:
    print(f"{min(abs(A-B),abs(L1[idx-1]-B)+1)}")
else:
    print(f"{min(abs(L1[idx]-B)+1,abs(A-B),abs(L1[idx-1]-B)+1)}")