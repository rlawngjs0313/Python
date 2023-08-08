N = int(input())
L1 = list(map(int, input().split()))
M = int(input())
L2 = list(map(int, input().split()))
L1.sort(reverse=True)
L2.sort(reverse=True)
if L1[0] < L2[0]:
    print(-1)
    exit()

result = 0
while True:
    if L2 == []:
        print(result)
        exit()
    for i in L1:
        for idx, j in enumerate(L2):
            if i >= j:
                L2.pop(idx)
                break
    result += 1