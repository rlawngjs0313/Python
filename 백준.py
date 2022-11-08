import sys

N = int(input())
A_List = list(map(int, sys.stdin.readline().split()))
B_List = list(map(int, sys.stdin.readline().split()))
AResultList = [0 for _ in range(N)]
result = 0

for i in range(N):
    mx = max(B_List)
    mn = min(A_List)
    result += mx * mn
    A_List.pop(A_List.index(mn))
    B_List.pop(B_List.index(mx))

print(result)