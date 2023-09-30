#2563 구현 약 30:00

N = int(input())
L1 = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for _ in range(N):
    w, h = map(int, input().split())
    duple = 0
    for i in range(10):
        for j in range(10):
            if L1[w+i][h+j] != 0:
                duple += 1
            L1[w+i][h+j] += 1

    result += (100 - duple)

print(result)