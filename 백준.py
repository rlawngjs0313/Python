N = int(input())
while N > 0:
    a = [False] + [True] * (2*N-1)
    m = int((2*N)**0.5)

    for i in range(m + 1):
        if a[i] == True:
            for j in range(2*i+1, 2*N, i+1):
                a[j] = False
    a = a[N:]
    print(a.count(True))
    N = int(input())