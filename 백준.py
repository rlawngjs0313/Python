import sys

N, K = map(int, sys.stdin.readline().split())
result, cnt = 0, 1
L1 = []

for i in range(N):
    L1.append(int(sys.stdin.readline()))

while True:
    if K == 0:
        break
    elif K % L1[N-cnt] != K:
        result += K // L1[N-cnt]
        K %= L1[N-cnt]
    cnt += 1

print(result)