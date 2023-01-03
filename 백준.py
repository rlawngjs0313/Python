import sys

N = int(input())
L1 = [0 for _ in range(26)]
result = 0

for i in range(N):
    data = sys.stdin.readline().rstrip()
    length = len(data)-1
    for j in data:
        L1[ord(j) % 65] += 10**length
        length -= 1

L1.sort(reverse=True)

for i, j in zip(L1, range(9, 0, -1)):
    result += i*j

print(result)