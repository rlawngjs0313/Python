import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    lcm = math.lcm(M,N)
    if x == y and x <= min(M,N):
        print(f"{x}\n")
        continue
    while x != y and (x <= lcm and y <= lcm):
        if x > y:
            y += N
        else:
            x += M
    if x > lcm or y > lcm:
        print('-1\n')
    else:
        print(f"{x}\n")