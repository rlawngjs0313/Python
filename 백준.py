import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    A, B = max(A, B), min(A, B)
    temp = A*B
    if B == 1:
        sys.stdout.write(str(A) + '\n')
    else:
        while True:
            if A % B == 0:
                sys.stdout.write(str(int(temp/B)) + '\n')
                break
            else:
                A %= B
                A, B = max(A, B), min(A, B)