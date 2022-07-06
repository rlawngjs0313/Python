N = int(input())
L1 = list(range(1, N+1))

for i in L1:
    result = i
    for j in str(i):
        result += int(j)
    if result == N:
        print(i)
        break
    elif i == N:
        print(0)