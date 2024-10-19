H1, A1, H2, A2 = map(int, input().split())
P, S = map(int, input().split())

#C1 = 용사킬, C2 = 마왕킬
C1, C2 = H1//A2 if H1%A2 == 0 else (H1//A2)+1, H2//A1 if H2%A1 == 0 else (H2//A1)+1
if C1 < C2:
    print('gg')
    exit()
else:
    H2 -= ((C2)-1)*A1
    H1 -= ((C2)-1)*A2
    if H2 <= P:
        H2 += S
C1, C2 = H1//A2 if H1%A2 == 0 else (H1//A2)+1, H2//A1 if H2%A1 == 0 else (H2//A1)+1
if C1 < C2:
    print('gg')
else:
    print('Victory!')