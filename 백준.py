num = int(input())
cont = 1
minus_num = 0
while True:
    minus_num += cont*6
    if num == 1:
        print(1)
        break
    elif num - minus_num <= 1:
        print(cont+1)
        break
    else:
        cont += 1