N, K = map(int, input().split())
L1 = list(map(int, input().split()))
L2 = []

for idx, val in enumerate(L1):
    L2.append((val,idx+1))
L2.sort(key=lambda x:(x[0],x[1]),reverse=True)

L1 = []
for i in range(min(N,K)):
    L1.append(L2[i][1])
L1.sort()

for i in L1:
    print(i)
for i in range(K-len(L1)):
    print(0)
for i in range(N):
    if len(L1) > 0 and i+1 == L1[0]:
        print(i+1)
        L1.pop(0)
    else:
        print(0)