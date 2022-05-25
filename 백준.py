num = int(input())
cont = 1
minus_num = 0
while True:
    minus_num += cont
    if num == 1:
        print("1/1")
        break
    elif num - minus_num <= 0:
        if cont % 2 == 0:
            A = range(1, cont+1)
            B = range(cont, 0, -1)
            print(f"{B[minus_num-num]}/{A[minus_num-num]}")
        else:
            A = range(cont, 0, -1)
            B = range(1, cont+1)
            print(f"{B[minus_num-num]}/{A[minus_num-num]}")
        break
    else:
        cont += 1