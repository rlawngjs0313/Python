import sys
input = sys.stdin.readline
print = sys.stdout.write

INF = 1000000
prime = [0]*(INF+1)
for i in range(2,int(INF**0.5)+1):
    if prime[i] == 0:
        for j in range(i*i,INF+1,i):
            prime[j] = 1


T = int(input())
for _ in range(T):
    N = int(input())
    A, B = N//2, N//2
    result = 0
    while A != 1:
        if prime[A] == 0 and prime[B] == 0:
            result += 1
        A -= 1
        B += 1
    print(f"{result}\n")