import sys

N = int(input())
L1 = list(map(int, sys.stdin.readline().split()))
L1.sort()

result = [1]

last = result[-1]
for i in L1:
    if i > last:
        break
    else:
        last += i

print(last)