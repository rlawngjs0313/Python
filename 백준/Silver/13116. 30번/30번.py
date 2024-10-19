import sys

T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    while A != B:
        if A > B:
            A //= 2
        else:
            B //= 2
    sys.stdout.write(f"{A*10}\n")