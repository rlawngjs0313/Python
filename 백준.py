C = int(input())
for k in range(C):
    K = int(input())
    N = int(input())
    L1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    L2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(K):
        for j in range(N):
            if j == 0:
                L2[j] = L1[j]
            else:
                L2[j] = L2[j-1] + L1[j]
                L1[j] = L2[j]
    print(L2.pop(N-1))