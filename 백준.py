# 1966번 구현문제 23:57

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    L1 = list(map(int, input().split()))
    result = 0
    maxNum = max(L1)

    while True:
        if L1[0] == maxNum:
            if M == 0:
                print(result+1)
                break
            else:
                L1.pop(0)
                maxNum = max(L1)
                result += 1
                M -= 1
        else:
            L1.append(L1.pop(0))
            if M != 0:
                M -= 1
            else:
                M = len(L1)-1