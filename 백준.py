N = int(input())
L1 = list(range(666, 2666800))
while True:
    for i in L1:
        if '666' in str(i):
            N -= 1
            if N == 0:
                print(i)
                break
    if N == 0:
        break