N, M = map(int, input().split())
L1 = []
result = []
result_B = 0
result_W = 0
index = 0
for _ in range(N):
    data = tuple(input())
    L1.append(data)
for k in range(N-7):
    for l in range(0, M-7):
        for _ in range(k, k+8): # 8x8 하나 읽기
            for j in range(l, l+8, 2):
                if L1[_][j] == "W":
                    result_B += 1
                    if L1[_][j+1] == "B":
                        result_B += 1
                    else:
                        result_W += 1
                if L1[_][j] == "B":
                    result_W += 1
                    if L1[_][j+1] == "W":
                        result_W += 1
                    else:
                        result_B += 1
            index = result_B
            result_B = result_W
            result_W = index
        result.append(min(result_B, result_W))
        result_B, result_W, index = 0, 0, 0
print(f"{min(result)}")