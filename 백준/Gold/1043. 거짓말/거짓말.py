import sys

N, M = map(int, input().split())
L1 = list(map(int, input().split()))
L1 = set(L1[1:])
queue = []
result = 0

# M번 돌려서 진실 아는 사람 추가
for _ in range(M):
    L2 = list(map(int, sys.stdin.readline().split()))
    L2 = L2[1:]
    queue.append(L2)
    for i in L2:
        if i in L1:
            L1.update(L2)
            break
for _ in range(M):
    for i in queue:
        for j in i:
            if j in L1:
                L1.update(i)
                break

# 다시 돌리기
for i in queue:
    for j in i:
        if j in L1:
            break
    else:
        result += 1

print(result)