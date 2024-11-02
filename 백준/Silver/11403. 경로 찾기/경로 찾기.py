import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
INF = 1e8
L1 = []
for i in range(N):
    temp = []
    for j in list(map(int, input().split())):
        if j != 0:
            temp.append(1)
        else:
            temp.append(INF)
    L1.append(temp)

for i in range(N):
    for j in range(N):
        for k in range(N):
            L1[j][k] = min(L1[j][k], L1[i][k]+L1[j][i])

for i in L1:
    for j in i:
        print(f"{1 if j != INF else 0} ")
    print("\n")