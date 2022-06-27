C = int(input())
for i in range(C):
    H, W, N = map(int, input().split())
    H1 = int(N/H)+1
    if H%W == 0:
        if H1 < 10:
            print(f"{H}0{H1}")
        else:
            print(f"{H}{H1}")
    else:
        if H1 < 10:
            print(f"{N%H}0{H1}")
        else:
            print(f"{N%H}{H1}")