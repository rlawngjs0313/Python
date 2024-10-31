from collections import defaultdict
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
D1 = defaultdict(int)

word = list(map(int, input().split()))
result, start, end = 0, 0, 0
while end < N:
    if D1[word[end]] >= K:
        D1[word[start]] -= 1
        start += 1
    else:
        D1[word[end]] += 1
        end += 1
        result = max(result, end-start)
print(f"{result}")