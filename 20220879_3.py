import random
L = ['가위', '바위', '보']
win, com_win = 0, 0
while True:
    com_answ = random.randint(1, 3)
    answ = input('가위, 바위, 보 중 하나를 입력하시오 : ')
    if answ not in L:
        print('출력오류')
        continue
    print('컴퓨터: {}'.format(L[com_answ]))
    
    # 가위: 이김 = -2 짐 = -1  바위: 이김 = 1 짐 = -1  보: 이김 = 1 짐 = 2
    result = answ + com_answ
    if abs(result) > 1:
        result *= -1

    if result > 0:
        print("You WIN")
        win += 1
    elif result < 0:
        print("Com WIN")
        com_win += 1
    else:
        print("Draw")

    if win == 3:
        print('You WIN!!')
        break
    elif com_win == 3:
        print('컴퓨터 WIN!!')
        break