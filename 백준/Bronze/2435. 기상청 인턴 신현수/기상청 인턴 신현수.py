import sys
input = sys.stdin.readline
print = sys.stdout.write

N,K = map(int,input().split())
L1 = list(map(int,input().split()))
s = 0
e = s+K
result = sum(L1[s:e])
temp = result
for _ in range(N-e):
    temp -= L1[s]
    temp += L1[e]
    if e < N:
        result = max(result,temp)
        s += 1
        e += 1

print(f"{result}\n")