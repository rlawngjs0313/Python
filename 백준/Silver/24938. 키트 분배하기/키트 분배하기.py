import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = list(map(int,input().split()))
mid = sum(L1)//N

result = 0
for i in range(N-1):
    if L1[i] > mid:
        L1[i+1] += L1[i]-mid
        result += L1[i]-mid
    elif L1[i] < mid:
        L1[i+1] -= mid-L1[i]
        result += mid-L1[i]

print(f"{result}\n")