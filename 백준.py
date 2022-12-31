import sys

N = int(input())
L1 = []
result = 0

temp1 = list(map(int, sys.stdin.readline().split()))
temp2 = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    L1.append([temp1[i], temp2[i]])

L1.sort(key=lambda x:(x[1], x[0]))

while L1:
    for i in L1:
        

print(result)