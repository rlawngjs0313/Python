while True:
    L1 = list(map(int, input().split()))
    L1.sort()
    if L1[0] == L1[1] == L1[2] == 0:
        break
    if L1[0]**2 + L1[1]**2 == L1[2]**2:
        print("right")
    else:
        print("wrong")