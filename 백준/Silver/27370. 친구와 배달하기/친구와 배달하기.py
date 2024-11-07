import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    N, Pa, Pb = map(int, input().split())
    L1 = list(map(int, input().split()))
    L2, A, B = [], 0, 0
    for i in L1:
        if 2*(abs(i-Pa)) < 2*(abs(i-Pb)):
            A += 2*(abs(i-Pa))
        elif 2*(abs(i-Pa)) > 2*(abs(i-Pb)):
            B += 2*(abs(i-Pb))
        else:
            L2.append(2*(abs(i-Pb)))
    for i in L2:
        if A >= B:
            B += i
        else:
            A += i
    print(f"{A+B} {abs(A-B)}\n")