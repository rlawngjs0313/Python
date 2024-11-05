import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    n = int(input())
    L1 = [list(map(int, input().split())) for _ in range(2)]
    result = 0
    for j in range(1, n):
        for i in range(2):
            temp = L1[i-1][j-1]+L1[i][j]
            if 0<=j-2:
                temp = max(temp,max(L1[0][j-2],L1[1][j-2])+L1[i][j])
            L1[i][j] = temp
    print(f"{max(L1[0][-1],L1[1][-1])}\n")