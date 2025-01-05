import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M, K = map(int,input().split())
L1 = []

for _ in range(N):
    a,b = map(int,input().split())
    L1.append((a,b))
L1 = sorted(L1,key=lambda x:(x[1]))

result = 0
for _ in range(K):
    result += L1.pop()[0]

L1 = sorted(L1,key=lambda x:(x[0]))
for _ in range(M):
    result += L1.pop()[0]

print(f"{result}\n")