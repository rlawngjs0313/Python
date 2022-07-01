M = int(input())
while M > 1:
    for i in range(2, M+1):
        if M == i:
            print(i, end="\n")
            M = int(M/i)
            break
        elif M % i == 0:
            print(i, end="\n")
            M = int(M/i)
            break