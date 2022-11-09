import sys  # 1946번 신입 사원

T = int(input())

for _ in range(T):
    N = int(input())
    mx, result = 0, 0
    L1, temp = [], []
    for j in range(N):
        L1.append(list(map(int, sys.stdin.readline().split())))
    L1.sort(key=lambda x: (x[0]))
    # 엄
    print(result)