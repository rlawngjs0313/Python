import sys  # 1700번 도전

N, K = map(int, sys.stdin.readline().split())
L1 = list(map(int, sys.stdin.readline().split()))
L2 = []
result = 0

while len(L2) != N and L1 != []:
    temp = L1.pop(0)
    if temp not in L2:
        L2.append(temp)

while L1 != []:
    i = L1.pop(0)
    if i not in L2:
        L3 = []
        cnt = 0
        for j in L2:
            if j in L1:
                L3.append([-1*(L1.index(j)), cnt])
            else:
                L3.append([-(K+1), cnt])
            cnt += 1
        L3.sort(key=lambda x: (x[0]))
        del L2[L3[0][1]]
        L2.append(i)
        result += 1

print(result)