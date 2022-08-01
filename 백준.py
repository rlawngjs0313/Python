import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    data = deque(map(int, sys.stdin.readline().split()))
    n = data.popleft()
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            M, N = max(data[i], data[j]), min(data[i], data[j])
            while N != 0:
                temp = M%N
                (M,N) = (N,temp)
            result += abs(M)
    sys.stdout.write(str(result) + '\n')