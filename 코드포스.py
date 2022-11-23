import sys
sys.setrecursionlimit(100000)

t = int(input())

for i in range(t):
    n, q = map(int, sys.stdin.readline().split())
    L1 = list(map(int, sys.stdin.readline().split()))
    L2 = []
    
    cnt = 0
    for _ in range(n):
        if L1[cnt] % 2 == 0:
            L2.append(L1.pop(cnt))
        else:
            cnt += 1

    for _ in range(q):
        i, j = map(int, sys.stdin.readline().split())
        if i == 0:
            cnt = 0
            T1 = []
            for _ in range(len(L2)):
                temp = L2.pop() + j
                if temp % 2 == 0:
                    T1.append(temp)
                else:
                    L1.append(temp)
            L2 = T1
        else:
            cnt = 0
            T1 = []
            for _ in range(len(L1)):
                temp = L1.pop() + j
                if temp % 2 != 0:
                    T1.append(temp)
                else:
                    L2.append(temp)
            L1 = T1
        sys.stdout.write(str(sum(L1)+sum(L2)) + '\n')