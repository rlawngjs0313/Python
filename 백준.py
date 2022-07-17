import sys

def gcd(M, N):
    if M == N:
        return M
    elif M > N:
        return gcd(M-N, N)
    elif M < N:
        return gcd(M, N-M)
def lcm(M, N, gcd):
    return abs(M*N) / gcd

N, M = map(int, input().split())
sys.setrecursionlimit(1000000)
result = gcd(M, N)
print(result)
print(int(lcm(M, N, result)))