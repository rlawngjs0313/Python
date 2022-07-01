C = int(input())
for i in range(C):
    H, W, N = map(int, input().split())
    H1 = N%H
    H2 = N//H+1
    if H1 == 0:
        if H2 <= 10:
            print(f"{H}0{H2-1}")
        else:
            print(f"{H}{H2-1}")
    else:
        if H2 < 10:
            print(f"{H1}0{H2}")
        else:
            print(f"{H1}{H2}")