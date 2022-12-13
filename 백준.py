import sys

A, B = map(int, sys.stdin.readline().split())
result = 0

while A != B and A < B:
    if B % 2 == 0:
        B //= 2
        result += 1
    elif str(B)[-1] == '1':
        B //= 10
        result += 1
    else:
        print(-1)
        exit()

if A > B:
    print(-1)
else:
    print(result+1)