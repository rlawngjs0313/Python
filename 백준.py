N = int(input())
M = int(input())
L1 = []
result = abs(100 - N)

if M != 0:
    L1 = list(input().split())

for i in range(1000001): 
    for j in str(i):
        if j in L1:
            break
    else:
        result = min(result, len(str(i)) + abs(i - N))
print(result)