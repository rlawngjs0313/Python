R, C, W = map(int, input().split())
L1 = []
for i in range(1,R+W+1):
    temp = []
    for j in range(i):
        if j == 0 or j == i-1:
            temp.append(1)
        else:
            temp.append(L1[-1][j-1]+L1[-1][j])
    L1.append(temp)

result = 0
for i in range(W):
    for j in range(i+1):
        result += L1[R-1+i][C-1+j]

print(result)