N, A, B = map(int, input().split())
result = 1
L1 = list(range(1, N+1))

while len(L1) != 0:
    L2 = []
    for i in range(0, len(L1), 2):
        try:
            if (L1[i] == A and L1[i+1] == B) or (L1[i] == B and L1[i+1] == A):
                print(result)
                exit()
            elif L1[i] == A or L1[i+1] == A:
                A = (i+2)//2
            elif L1[i] == B or L1[i+1] == B:
                B = (i+2)//2
            L2.append((i+2)//2)
        except IndexError:
            if L1[i] == A:
                A = (i+2)//2
            elif L1[i] == B:
                B = (i+2)//2
            L2.append((i+2)//2)
    L1 = L2[:]
    result += 1