num = int(input())
cont = 1
minus_num = 0
while True:
    minus_num += cont
    if num == 1:
        print(cont, minus_num)
        break
    elif num - minus_num <= 0:
        print(cont, minus_num)
        break
    else:
        cont += 1