import sys
sys.setrecursionlimit(1000000)

def solution(n):
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4
    else: return solution(n-1) + solution(n-2) + solution(n-3)

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    sys.stdout.write(str(solution(n)) + '\n')