import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
L1 = []

for _ in range(n):
    word = list(map(int, input().split()))
    L1.append(word)

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            L1[i][j] += L1[i-1][j]
        elif j == i:
            L1[i][j] += L1[i-1][j-1]
        else:
            L1[i][j] += max(L1[i-1][j-1],L1[i-1][j])

print(f"{max(L1[-1])}\n")