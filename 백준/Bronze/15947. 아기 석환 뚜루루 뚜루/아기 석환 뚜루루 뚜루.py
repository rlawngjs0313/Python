L1 = [("", "baby", "sukhwan"), ("", "very", "cute"), ("", "in", "bed")]

N = int(input())
if N % 14 == 0:
    print(L1[((N%14)//4)%3][((N%14)+2)%4])
    exit()
if (N%14) % 4 == 3:
    if N // 14 >= 3:
        print(f"tu+ru*{(N//14)+2}")
    else:
        print(f"tu{'ru'*((N//14)+2)}")
elif (N%14) % 4 == 0:
    if N // 14 >= 4:
        print(f"tu+ru*{(N//14)+1}")
    else:
        print(f"tu{'ru'*((N//14)+1)}")
else:
    print(L1[((N%14)//4)%3][(N%14)%4])