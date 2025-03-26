import sys
input = sys.stdin.readline
print = sys.stdout.write

K, N = map(int,input().split())
L1 = []
for _ in range(K):
    L1.append(int(input()))

L1.sort()

s,e = 1, L1[-1]
while s<=e:
    result = 0
    m = (s+e)//2
    for i in L1:
        result += i//m
    if result >= N:
        s = m+1
    else:
        e = m-1

print(f"{e}\n")