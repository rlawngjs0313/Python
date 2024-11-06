import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M, K = map(int, input().split())
team = min(N//2,M)
remain = K-((N-team*2)+(M-team))
while remain > 0:
    team -= 1
    remain -= 3
print(f"{team}\n")