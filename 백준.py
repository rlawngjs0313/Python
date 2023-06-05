import sys

N, M = map(int, sys.stdin.readline().split())
L1 = [[] for _ in range(M)]
result = []
result_count = 0

for _ in range(N):
    data = sys.stdin.readline().rstrip()
    for idx, value in enumerate(data):
        L1[idx].append(value)

for i in range(M):
    L1[i].sort()
    result.append(max(L1[i], key=L1[i].count))
    while result[i] in L1[i]:
        L1[i].remove(result[i])
    result_count += (len(L1[i]))

print(str(result).replace("[", "").replace("]", "").replace("'", "").replace(", ", ""))
print(result_count)
