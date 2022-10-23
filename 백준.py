S = int(input())
cnt = 1
if S == 1:
    print(1)
else:
    while True:
        S -= cnt
        if S == 0:
            print(cnt)
            break
        elif S < 0:
            print(cnt-1)
            break
        else:
            cnt += 1