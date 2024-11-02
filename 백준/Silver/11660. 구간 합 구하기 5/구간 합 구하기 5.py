import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
L1 = []

for i in range(N):
    word = list(map(int, input().split()))
    temp = []
    for j in range(N):
        if 0<=i-1 and 0<=j-1:
            temp.append(word[j]+temp[j-1]+L1[i-1][j]-L1[i-1][j-1])
        elif 0<=i-1:
            temp.append(word[j]+L1[i-1][j])
        elif 0<=j-1:
            temp.append(word[j]+temp[j-1])
        else:
            temp.append(word[j])
    L1.append(temp)

for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split())
    A = L1[N-1][N-1]-L1[x2-1][y2-1]
    B1,B2 = 0,0
    if 0<=y1-2:
        B1 = L1[x2-1][y1-2]
    if 0<=x1-2:
        B2 = L1[x1-2][y2-1]
    if B1 != 0 and B2 != 0:
        B2 -= L1[x1-2][y1-2]
    print(f"{L1[N-1][N-1]-(A+B1+B2)}\n")