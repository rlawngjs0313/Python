from collections import defaultdict
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    D1 = defaultdict(int)
    N = int(sys.stdin.readline())
    for i in list(map(int, sys.stdin.readline().split())):
        D1[i] = 1
    M = int(sys.stdin.readline())
    for i in list(map(int, sys.stdin.readline().split())):
        if D1[i] == 1:
            print(1)
        else:
            print(0)