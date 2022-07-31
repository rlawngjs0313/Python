import sys

def solution(N, M):
    cnt = 0
    while N != 0:
        N = N//M
        cnt += N
    return cnt

n, m = map(int, sys.stdin.readline().split())

print(min(solution(n, 2) - solution(m, 2) - solution(n-m, 2), solution(n, 5) - solution(m, 5) - solution(n-m, 5)))