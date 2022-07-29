import sys

data = sys.stdin.readline().rstrip()
result = [0] * 26

for i in data:
    result[ord(i)-ord("a")] += 1
print(*result)