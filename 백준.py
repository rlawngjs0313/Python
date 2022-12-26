import sys

N = int(input())
L1 = []
result = 0

temp1 = list(map(int, sys.stdin.readline().split()))
temp2 = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    L1.append([temp1[i], temp2[i]])

minX = min(temp1)
L1.sort(key=lambda x:(x[0], x[1]))

while L1:
    if L1[0][0] >= L1[0][1] and L1[0][0] == minX:
        L1.pop(0)
    else:
        while L1[0][0] < L1[0][1]:
            for i in L1:
                if i[0] < i[1]:
                    i[0] += 30
                    result += 1
        L1.sort(key=lambda x:(x[0], x[1]))
                
            
print(result)