from math import log2

N = int(input())
result = int(log2(N))
if N == 1:
    print(1)
elif N == 2**result:
    print(N)
else:
    print(2*(N%(2**result)))