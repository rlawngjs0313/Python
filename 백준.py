N, M = map(int, input().split())
L = list(map(int, input().split()))
num = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            newNum = (L[i]+L[j]+L[k])
            if num <= newNum <= M:
                num = newNum
print(num)