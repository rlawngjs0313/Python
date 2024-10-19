N = int(input())
A = list(map(int, input().split()))
result = [0]*N

cnt = 0
for i in sorted(list(set(A))):
    for idx,val in enumerate(A):
        if val == i:
            result[idx] = cnt
            cnt += 1

print(*result)