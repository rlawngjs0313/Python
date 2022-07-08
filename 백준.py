N = int(input())
L1 = []

for i in range(N):
    L1.append(int(input()))
    while (i>0) and (L1[i] < L1[i+1]):
        L1[i], L1[i-1] = L1[i-1], L1[i]
        i -= 1

for i in L1:
    print(i)